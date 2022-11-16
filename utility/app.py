from selenium.webdriver.common.by import By
from src import FileHandle, AuthConnection, random_company, urlparsers
import sys, time, os
from urllib.parse import *
from dotenv import load_dotenv
load_dotenv()

# connections = int(input(f"How many conncetion you want?: "))
connections = 10
page, count = 0, 0


def main():
    global page
    global count
    
    elementId, element_blacklist, old_element_backlist = 0, [], []
    filehandle = FileHandle('elementsId.txt')
    list_element = driver.find_elements(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']/span[@class='artdeco-button__text']")
    list_of_old_elements = filehandle.readfile(old_element_backlist)
    
    for element in list_element:
                
        if element.get_attribute('innerHTML').strip() == 'Connect':
            try:
                elementId = element.id
                if elementId not in list_of_old_elements:
                    elementId = str(element.id)
                    element_blacklist.append(elementId)
                    element.click()
                    time.sleep(2)
                    for handle in driver.window_handles:
                        driver.switch_to.window(handle)
                        for pops in driver.find_elements(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml1']/span[@class='artdeco-button__text']"):
                            try:
                                pops.click()
                                time.sleep(2)
                            except:
                                driver.refresh()
            except:
                print("Didn't pass click list of element ")
            
            count +=1
            if count >= connections:
                try:
                    sys.exit(0)
                except Exception as e:
                    print(e)
            else:
                print(f"Connections number: {count}")
    if elementId not in list_of_old_elements:
        filehandle.writetofile(element_blacklist)
        
    print(f"[ INFO ] Bot send {count} connections")
    
    if count < connections or len(list_element) == 0:
        page +=1
        print(f"searching element next page {page}")
        url2 = urlparsers(obj[0].strip(), page)
        print(url2)
        driver.get(url2)
        time.sleep(2)
        main()
        
    print("Closing app.py, exiting ....")
    driver.close()
        
if __name__=='__main__':
    obj = random_company("./fortune.txt")
    url2 = urlparsers(obj[0].strip(), page)
    print(url2)
    print(f"Will find connection in {obj[0].strip()} company")
    auth = AuthConnection(url2)
    if os.path.isfile("cookies.pkl"):
        driver = auth.continue_session()
    else:
        driver = auth.login()
    
    main()
    