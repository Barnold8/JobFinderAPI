from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
import json
import classes


app = Flask(__name__)
api = Api(app)

sites = {
    "indeed": classes.Indeed,
    "totaljobs":classes.TotalJobs
}

        # args are case sensitive
job_get_args = reqparse.RequestParser()
job_get_args.add_argument("where",type=str,help="Location of the user is required <City/Postcode/Zip code>",required = True)
job_get_args.add_argument("what", type=str,help="Name of the job e.g. Carer, IT, Retail, Software engineer, Manager is required",required = True)
# add pages arg here, NOT REQUIRED (required = False)

def abort_if_not_job(job:str):
    if job.lower() not in sites:
        abort(404,message=f"Job '{job}' isn't a requestable site on this API.")

class Job(Resource):
    def get(self,job_site):
        args = job_get_args.parse_args()

        abort_if_not_job(job_site)

        job_parser = sites["indeed"]([args["what"],args["where"]])

        job_parser.quit()

        return {job_site: args}


api.add_resource(Job, '/Job/<string:job_site>')

if __name__ == "__main__":
    
    settings = json.load(open("config/settings.json"))

    app.run(host=settings["API"]["host"], port=settings["API"]["port"], debug=settings["API"]["debug_mode"])