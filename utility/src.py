from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os, random, pickle
from urllib.parse import *
from dotenv import load_dotenv
load_dotenv()

url = "https://linkedin.com"
username = "3237369412"
password = os.getenv("password")



class FileHandle():
    def __init__(self, file_name):
        self.file_name = file_name
        
        
    def writetofile(self,element_list):    
        with open(self.file_name, 'a') as filehandle:
            for element in element_list:
                filehandle.writelines(f"{element}\n")
                
                
    def readfile(self, element_list_from_file):
        # Open the file and read the content in a list
        with open(self.file_name, 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                # Remove linebreak which is the last character of the string
                curr_place = line[:-1]
                 # Add item to the list
                element_list_from_file.append(curr_place)
            return element_list_from_file
              
              
class AuthConnection():
    print("Login to Linkedin...")
    def __init__(self, url):
        self.url = url
    
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object)
    driver.get(url)
    
    def continue_session(self):
        try:           
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            for i in range(5):
                time.sleep(1)
                print(f"Closing session in {i} minutes")
            self.driver.close()
                
        return self.driver
    
    def login(self):
        try:
            self.driver.find_element(By.ID,"session_key").send_keys(username) 
            self.driver.find_element(By.ID,"session_password").send_keys(password)
            self.driver.find_element(By.CLASS_NAME,"sign-in-form__submit-button").send_keys(Keys.ENTER)
            pickle.dump( self.driver.get_cookies() , open("cookies.pkl","wb"))
        except:
            for i in range(4):
                print(f"Closing session in {i} minutes")
            self.driver.close()
        
        return self.driver



def urlparsers(target, page):
    par = ParseResult(
        scheme='https', 
        netloc='www.linkedin.com', 
        path='/search/results/people/',
        params='', 
        query='keywords=IT%20recruiter%20' + target + '&origin=GLOBAL_SEARCH_HEADER&page=' + str(page) + '&sid=""', 
        fragment='')
    
    unparse_url = urlunparse(par)
    return unparse_url

def random_company(file):
    with open(file,"r") as f: 
        data = list(f.readlines())
        random_company = random.sample(data,k=1)
    return random_company


if __name__=='__main__':
    obj = random_company()
    print(urlparsers(obj[0].strip(), 4))