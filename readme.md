<a href=https://github.com/Barnold8>
<img src="https://avatars.githubusercontent.com/u/55092542?v=4" alt="Aimeos logo" title="Aimeos" align="right" height="150"/>
</a>

# Job finder API.

# What is it?

The job finder API is a mechanism to provide ease of use in regards to finding jobs programmatically. This repository is aimed at applications that wish to query multiple job websites for, well, jobs! An example in mind would be an application that allows a user to pick job websites from a checklist, provide their location and then the role they wish to embark upon. After this, on their end theyll get a whole massive list of jobs, but behind the scenes, this API will scrape job websites with specific paramitized data that the user gave. However, this can be used however you please **(I AM NOT RESPONSIBLE FOR THE USE OF THIS API BY EXTERNAL PARTIES THAT AREN'T ME)
**

<details>
<summary><h3>Requirements.</h3></summary>

```
  Selenium 4.11.2 - Used to scrape websites for data
  undetected-chromedriver 3.5.2 - Used to get past basic cloudflare bot protection
  Flask 2.3.2 - Used to facilitate API
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
  
  > An sample request would look like:
  > > GET http://127.0.0.1:8000/Job/indeed?what=care&where=London&pages=1
  <details>
  <summary><h3>Sample response **(Not real data)**</h3></summary>

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



</details>

<details>
<summary><h3> Supported sites </h3></summary>

* Indeed.com

</details>



