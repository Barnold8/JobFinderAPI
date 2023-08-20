<a href=https://github.com/Barnold8>
<img src="https://avatars.githubusercontent.com/u/55092542?v=4" alt="Aimeos logo" title="Aimeos" align="right" height="150"/>
</a>

# Job finder API.

# What is it?

The job finder API is a mechanism to provide ease of use in regards to finding jobs programmatically. This repository is aimed at applications that wish to query multiple job websites for, well, jobs! An example in mind would be an application that allows a user to pick job websites from a checklist, provide their location and then the role they wish to embark upon. After this, on their end theyll get a whole massive list of jobs, but behind the scenes, this API will scrape job websites with specific paramitized data that the user gave. However, this can be used however you please **(I AM NOT RESPONSIBLE FOR THE USE OF THIS API BY EXTERNAL PARTIES THAT AREN'T ME)**

<details>
<summary><h3>Requirements.</h3></summary>

```
  Python 3.10.8
  Selenium 4.10.0 - Used to scrape websites for data
  undetected-chromedriver 3.5.2 - Used to get past basic cloudflare bot protection
  Flask 2.2.2 - Used to facilitate API
  Flask-RESTful 0.3.10 - Used to help make API RESTful
```
> Using  pip install -r requirements.txt will fix any dependency issues

</details>

<details>
<summary><h3>How to use the API.</h3></summary>

  This API has **one** endpoint due to its simple nature. This endpoint is called **_Job_**. This endpoint takes a job website name as the URI and three variables.
  The three variables are as follows:
  
  * where: Location of the user, used to find jobs close to them
  * what: The desired job role of the user, used to find jobs relating to their desired job role
  * pages: The amount of jobs that are parsed from the given site

  By default, these variables are required. However, even though it is not recommended, these variables can become optional if you set the corresponding booleans to false in the configuration file provided. To see more information on this see [Configuration file](#config)
  
  <details>
    
  <summary><h4> GET requests </h4></summary>
  
  > A sample request would look like:
  > > GET http://127.0.0.1:8000/Job/indeed?what=care&where=London&pages=1

  > If you want to try sending a request with curl, the request will look like 
  > > curl -X GET -H "Content-Type: application/json" -d "{}" "127.0.0.1:8000/Job/indeed?what="Software"&where="London"&pages=2"
  > > > Note: the host and port will be different depending on what is stored in settings.json. 
        Content type being json is just a weird Flask RESTful thing to allow requests
  <details>
  <summary><h4>Sample response <b>(Not real data)</b></h4></summary>

  ```json
  {
      "Job data": [
          {
              "name": "Johns care institute",
              "company": "JCI",
              "location": "Fake west st",
              "link": "https://cataas.com/cat/says/hello%20world!"
          },
          {
              "name": "Veterinary Receptionist",
              "company": "Vets R us",
              "location": "Northampton silly billy st",
              "link": "https://genrandom.com/cats/"
          }
      ]
  }
```
</details>

</details>
</details>


<details>
<summary name="config"><h3> Configuration file </h3></summary>

  The configuration file allows customisation of the API and the website parser to meet the needs of your application. 
  The config.json file looks like and can be found [here](https://github.com/Barnold8/JobFinderAPI/blob/main/config/settings.json)
```json
{
    "sites":{
        
        "indeed":{
            "tab_title" : "indeed" 
        },
        
        "totaljobs":{
            "tab_title" : "vacancies"
        }
        
    },
    "API":{
        
        "host": "0.0.0.0",
        "port": 8000,
        "job_name_required": true,
        "user_location_required": true,
        "page_amount_required": true,
        "debug_mode": true
        

    }
}
```

<details>
<summary><h4> The sites section </h4></summary>

The **sites** section relates to classes.py. Each job website that is supported will require a **tab title**. A tab title is the title you see within the tab. The tab titles in the settings file are a substring, the substring pertaining to the website is what can be expected within the tab title on a successful query. This is used to ensure that the website has fully loaded before data is scraped off of the page.

</details>

<summary><h4> The API section </h4></summary>

The **API** section relates to the configurations that can be made for the API. These are basic things like the host or port. On top of this, there are a set of booleans that can be true or false. By default they are all true (this is recommended,except debug mode which shouldn't be on in production environments). The booleans work as follows

* job_name_required - Job endpoint requires the variable "what" to be filled in
* user_location_required - Job endpoint requires the variable "where" to be filled in
* page_amount_required - Job endpoint requires the variable "pages" to be filled in
* debug_mode - Allows for debug output in the console for the API server

</details>

</details>





</details>

<details>
<summary><h3> Supported sites </h3></summary>

* [Indeed.com](https://indeed.com/)
* [TotalJobs](https://www.totaljobs.com/)

</details>



