from selenium import webdriver
from selenium.webdriver.common.by import By


class Link:

    def __init__(self,protocol: str,domain: str,tl_domain: str,params: list[str]) -> None:
        """
       @author    : Brandon Wright

       Link class constructor

       :protocol: 
        
        
        """
        self.protocol = protocol
        self.domain = domain
        self.tl_domain = tl_domain
        self.params = params
    
    def replace_all(self,text, conditions):
        for i, j in conditions.items():
            text = text.replace(i, j)
        return text

    def URL_encode(self) -> None:
        conditions = {" ": "%20", ",": "%2C"}
        self.params = [self.replace_all(param, conditions) for param in self.params]

    def complete(self):
        return f"{self.protocol}://www.{self.domain}.{self.tl_domain}/{''.join(self.params)}"

class JobSite:

    def __init__(self) -> None:
        self.browser =  webdriver.Chrome()

    def makeRequest(self,href: Link, depth: int) -> None:
        
        self.browser.get(href.complete())

        pass

    def quit(self)-> None:
        self.browser.quit()






