from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://issues.apache.org/jira/browse/CAMEL-10597")
driver.maximize_window()

details1 = driver.find_element(By.XPATH,"//*[@id='issuedetails']/li[1]/div/strong").text

details2 = driver.find_element(By.XPATH,"//span[@id='type-val']").text

people1 = driver.find_element(By.XPATH,"//dt[normalize-space()='Assignee:']").text

people2 = driver.find_element(By.XPATH,"//span[@id='issue_summary_assignee_davsclaus']").text

dates = driver.find_element(By.XPATH,"//dt[normalize-space()='Created:']").text

date = driver.find_element(By.XPATH,"//*[@id='created-val']/time").get_attribute("datetime")

desciption = driver.find_element(By.XPATH,"//h4[normalize-space()='Description']").text

desciption1 = driver.find_element(By.XPATH,"//p[normalize-space()='Assume I have rest path']").text

comment = driver.find_element(By.XPATH,"//a[normalize-space()='Comments']").text

comment1 = driver.find_element(By.XPATH,"//a[@id='commentauthor_15748543_verbose']").text


commentDate = driver.find_element(By.XPATH,
    "//*[@id='comment-15748543']/div[1]/div[1]/div[2]/span/span/time").get_attribute("datetime")

comment2 = driver.find_element(By.XPATH,
    "//p[normalize-space()='GitHub user bobpaulin opened a pull request:']").text


path = "Assessment.csv"
file =open(path,'w')
writer = csv.writer(file)
writer.writerow([details1,people1,dates,desciption,comment])
writer.writerow([details2,people2,date,desciption1,comment1,commentDate,comment2])

print("finished")
