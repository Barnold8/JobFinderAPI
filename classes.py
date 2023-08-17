from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import undetected_chromedriver as uc 
import time
class Link:

    def __init__(self,protocol:str,domain:str,tl_domain:str,params:list[str]) -> None:
        """
       @author    : Barnold8

       :protocol: This is used to specify the section of the web address for what protocol
                  we are using. In this API, it is more often than not going to be HTTPS.
                  Having modularity allows for protocol changes if need be
       
       :domain:   This is used to actually say what domain the link pertains to. 
                  Stuff like 'Indeed', 'Reed' would go here.

       :tl_domain: This is used to specify the top level domain. Websites may use .com, 
       .co.uk, .org or any other variant.

       :params:  This is used to define all of the web address parameters that one would
                use on one of these sites for their query. Things like location, job
                distance to location among other things will be considered here. 
        
        :return: None

        """
        self.protocol = protocol
        self.domain = domain
        self.tl_domain = tl_domain
        self.params = params
    
    def replace_all(self,text:str, conditions:dict) -> str:
        """
        @author    : Barnold8

        This function takes a string input and formats it based on
        the conditions passed into it. 

        :text:     This is the original string that is passed in to be formatted
                   regarding the conditions
        
        :conditions: These conditions are key value pairs that are used to replace words.
                     For example, if you have the dict {" ": "abc"}, it will replace all 
                     instances of spaces within the string with "abc"

        :return: str
            
        """

        for i, j in conditions.items():
            text = text.replace(i, j)
        return text

    def URL_encode(self) -> None:
        """
        @author    : Barnold8

        This function converts its parameters into a URL compatible format.
        For example, spaces would be converted to "%20". See:
        https://www.w3schools.com/tags/ref_urlencode.ASP for more information.
            
        :return: None
            
        """

        conditions = {" ": "%20", ",": "%2C"}
        self.params = [self.replace_all(param, conditions) for param in self.params]

    def complete(self):
        return f"{self.protocol}://www.{self.domain}.{self.tl_domain}/{''.join(self.params)}"

class JobSite:
    
    # self note, depth will be in the actual website class 
    # so the website class can handle button clicks 

    WAIT_TIMER = 15

    def __init__(self) -> None:

        options = uc.ChromeOptions() 
        # options.headless = True 
        self.browser = uc.Chrome(use_subprocess=True, options=options)

    def makeRequest(self,href: Link, title:str,tag:str) -> WebElement:
        """
        @author: Barnold8
        
        makeRequest works by encoding the given link and then
        using the selenium library to make a GET request to 
        a website. WebDriverWait is used to ensure the site 
        is loaded before grabbing data from the page. 
        This is ensured by checking the passed in title is 
        a substring of the actual website title. 

        :href: A Link object to work with the browser "get" function. 
               (The complete method is used to pass a string to the 
               get function)

        :title: The title parameter is used to ensure that the webpage
                has loaded. This is done by making the webdriver 
                wait until the tab title includes the title parameter.
                The title given can even be a sub string of the actual full
                title, stopping ambiguity in its track with website title names.

        :tag:   Tag is used to configure what tag we are looking at on the 
                webpage. This makes it so you can choose the body, the head
                or alternatively you can pick html and get the entire source

        :return: This function returns a WebElement object. This is specified
        to one of the core tags on the page like the body or the head. 
        Alternatively you can pick the html tag to get the entire source
        
        """
        href.URL_encode()
        self.browser.get(href.complete())
        
        WebDriverWait(self.browser,JobSite.WAIT_TIMER).until(lambda driver: title in driver.title.lower() )

        return self.browser.find_element(By.TAG_NAME,tag)

    def grabPages(self,pages:int)-> list[WebElement]:
        """
        @author: Barnold8
        
        grabPages takes an amount of pages and returns a list of pages to
        process. 

        :pages: The amount of pages to grab. 

        :return: NotImplementedError - Forces subclasses to 
        implement their own solution as to make the developer
        (me) make the code work as needed for grabbing pages off of
        websites.

        """
        
        raise NotImplementedError

    def grabSource(self,href: Link, title:str,tag:str):
        """
        @author: Barnold8
        
        grabSource works like grabPages but it returns the literal
        HTML instead of a webElement object. It also only returns one 
        value rather than a list. 

        :pages: The amount of pages to grab. 

        :return: Returns a list of WebElements which allows for 
        processing on specific components of web pages.
        
        """
        return self.makeRequest(href,title,tag).get_attribute("outerHTML")
    
    def quit(self)-> None:
        """
        @author: Barnold8

        Closes the browser instance

        :return: None
        
        """
        self.browser.quit()


class Indeed(JobSite):

    def __init__(self,site_params) -> None:
        super().__init__()
        self.link = Link("https","indeed","com",site_params)
        self.website = self.makeRequest(self.link,"indeed","body")


    def grabPages(self, pages: int) -> list[dict]:
        """
        @author: Barnold8
        
        grabPages takes an amount of pages and returns a list of pages to
        process. 

        :pages: The amount of pages to grab. 

        :return: Returns a list of WebElements which allows for 
        processing on specific components of web pages.
        
        """
        job_data = []
        page = 1

        self.link.params.append("")
        while page <= pages:
            jobs = self.website.find_elements(By.CLASS_NAME, "cardOutline ")
            for job in jobs:
                try:
                    parsed_job = {
                        "name": job.find_element(By.TAG_NAME, 'span').get_attribute('title'),
                        "company": job.find_element(By.CLASS_NAME, 'companyName').get_attribute('innerText'),
                        "location": job.find_element(By.CLASS_NAME, 'companyLocation').get_attribute('innerText'),
                        "link": job.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    }
                    job_data.append(parsed_job)
                except Exception:
                    pass # ignore errors - Its because they are most likely related to an element being non existant, thus we can use this to ignore that.
            
            page += 1
            self.link.params[len(self.link.params)-1] = f"&start={(page-1)*10}"
            self.link.URL_encode()
            self.website = self.makeRequest(self.link,"indeed","body")

        return job_data

class TotalJobs(JobSite):

    def __init__(self,site_params) -> None:
        super().__init__()
        self.link = Link("https","totaljobs","com",site_params)
        self.website = self.makeRequest(self.link,"vacancies","body")

    def grabPages(self, pages: int) -> list[dict]:
        
        job_data = []
        page = 1
        self.link.params.append("")
        while page <= pages:
            self.website = self.makeRequest(self.link,"vacancies","body")
            jobs = self.website.find_elements(By.CSS_SELECTOR,"[data-at='job-item']")
            
            for job in jobs:
         
                try:
                    parsed_job = {
                        "name": job.find_element(By.CSS_SELECTOR,"[data-at='job-item-title']").get_attribute("innerText"),
                        "company": job.find_element(By.CSS_SELECTOR,"[data-at='job-item-company-name']").get_attribute("innerText"),
                        "location": job.find_element(By.CSS_SELECTOR,"[data-at='job-item-location']").get_attribute("innerText"),
                        "link": job.find_element(By.CSS_SELECTOR,"[data-at='job-item-title']").get_attribute("href")
                    }
                    job_data.append(parsed_job)
                except Exception:
                    pass # ignore errors - Its because they are most likely related to an element being non existant, thus we can use this to ignore that.

            page += 1



