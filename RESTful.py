from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

sites = ["indeed","totaljobs"]


def abort_if_not_job(job:str):
    if job.lower() not in sites:
        abort(404,message=f"Job '{job}' isn't a requestable site on this API.")

class Job(Resource):
    def get(self,job_site):
        abort_if_not_job(job_site)
        return {job_site: "Y"}


api.add_resource(Job, '/Job/<string:job_site>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)