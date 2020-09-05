import csv, smtplib, ssl
from time import sleep

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id("identifierId").send_keys("youremail")
driver.find_element_by_xpath("//span[contains(@class, 'RveJvd snByac')]").click()
sleep(4)
driver.find_element_by_xpath("//input[contains(@class, 'whsOnd zHQkBf')]").send_keys("yourpassword")
driver.find_element_by_xpath("//span[contains(@class, 'RveJvd snByac')]").click()
sleep(2)


with open("utenti.csv") as file:
        reader = csv.reader(file)
       # next(reader)  # Skip header row
        for name, email in reader:
            
            driver.find_element_by_xpath("//div[contains(@class, 'T-I T-I-KE L3')]").click()
            sleep(2)
            driver.find_element_by_xpath("//textarea[contains(@name, 'to')]").send_keys(email)
            driver.find_element_by_xpath("//input[contains(@name, 'subjectbox')]").send_keys("oggetto " +name.replace("ï»¿", "")+"")
            driver.find_element_by_xpath("//div[contains(@role, 'textbox')]").send_keys("Ciao "+name.replace("ï»¿", "")+","+" testo")
            driver.find_element_by_xpath("//div[contains(@class, 'T-I J-J5-Ji aoO v7 T-I-atl L3')]").click()


            
