from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import pyautogui
import time

print("Enter Email : ")
emailID = input()
password = pyautogui.password(text='', title='', default='', mask='*')
    
driver = webdriver.Chrome(executable_path="C:\\coding\\Assignment 4\\chromedriver.exe")
driver.get("https://opstra.definedge.com/")
driver.maximize_window()
driver.implicitly_wait(20)

# Login
driver.find_element_by_xpath("//body/div[@id='app']/div[2]/nav[1]/div[1]/div[4]/button[1]").click()
driver.find_element_by_xpath("//input[@id='username']").send_keys(emailID)
driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
driver.find_element_by_xpath("//input[@id='kc-login']").click()

# Strategy Builder
driver.find_element_by_xpath("//body/div[@id='app']/div[8]/nav[1]/div[1]/div[4]/div[2]/div[1]/button[1]").click()
driver.find_element_by_xpath("//body/div[@id='app']/div[5]/div[1]/div[9]/a[1]").click()

# Select Option Chains
driver.find_element_by_xpath("//body/div[@id='app']/div[62]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[3]/ul[1]/li[1]/div[1]/div[2]/i[1]").click()

# Function To Extract Data
def table():
    
    CallLTP = []
    ITM_Prob = []
    CallIV = []
    CallDelta = []
    StrikePrice = []
    PutDelta = []
    PutIV = []
    ITMProb = []
    PutLTP = []
    
    first = driver.find_elements_by_xpath("//td[@class='text-xs-center font-weight-bold body-1 blue--text']/div")
    last = driver.find_elements_by_xpath("//td[@class='text-xs-center font-weight-bold body-1 orange--text']/div")
    third = driver.find_elements_by_xpath("//td[@class='text-xs-center font-weight-bold body-1 ']")
    rows_index = driver.find_elements_by_xpath("//td[@class='text-xs-center font-weight-bold body-1']")
    
    total_rows = len(driver.find_elements_by_xpath("//tbody/tr"))

    for i in range(0,total_rows):
        CallLTP.append(first[i].text)
        ITM_Prob.append(rows_index[6*i].text)
        CallIV.append(third[i].text)
        CallDelta.append(rows_index[6*i+1].text)
        StrikePrice.append(rows_index[6*i+2].text)
        PutDelta.append(rows_index[6*i+3].text)
        PutIV.append(rows_index[6*i+4].text)
        ITMProb.append(rows_index[6*i+5].text)
        PutLTP.append(last[i].text)

    # Make Dataframe
    data = {"CallLTP":CallLTP, "ITM Prob.":ITM_Prob, "CallIV":CallIV, "CallDelta":CallDelta, "StrikePrice":StrikePrice, "PutDelta":PutDelta, "PutIV":PutIV, "ITMProb.":ITMProb, "PutLTP":PutLTP}
    df = pd.DataFrame(data)
    
    # Convert Dataframe Into .csv file
    file_name = Xpaths[j].text
    df.to_csv(file_name + ".csv")
    
# Select Dates
Dates = driver.find_elements_by_xpath("//div[@class='flex xs4 sm2 md1']/button")
Xpaths = driver.find_elements_by_xpath("//div[@class='flex xs4 sm2 md1']/button/div")

# Get Data
time.sleep(1)
for j in range(0,10):
    Dates[j].click()
    # WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//td[@class='text-xs-center font-weight-bold body-1 blue--text']/div")))
    time.sleep(1)
    table()
