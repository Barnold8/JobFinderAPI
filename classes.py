from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Link:

    def __init__(self,protocol:str,domain:str,tl_domain:str,params:list[str]) -> None:
        """
       @author    : Barnold8

       Link class constructor

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

    def __init__(self) -> None:
        self.browser =  webdriver.Chrome()

    def makeRequest(self,href: Link, title:str,tag:str) -> None:

        
        # self note, depth will be in the actual website class 
            # so the website class can handle button clicks 
        
        self.browser.get(href.complete())
        
        WebDriverWait(self.browser,15).until(lambda driver: title in driver.title )

        return self.browser.find_element(By.TAG_NAME,tag).get_attribute("outerHTML")



    def quit(self)-> None:
        self.browser.quit()






