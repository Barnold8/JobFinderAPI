from classes import *

J = JobSite()

link = Link("https","indeed","com",[])

request = J.makeRequest(link,"Job","body")
print(request)
