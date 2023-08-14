from classes import *

J = JobSite()

link = Link("https","indeed","com",["jobs?","q=care","&l=Nottingham"])

request = J.makeRequest(link,"Job","body")
print(request)
