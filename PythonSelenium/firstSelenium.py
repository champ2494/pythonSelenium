import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
# get the count of radio button
count_radiobutton = driver.find_elements_by_css_selector(".radioButton")
print(len(count_radiobutton))
# click the second radio btn
count_radiobutton[1].click()
# Handle autosuggestion
wait = WebDriverWait(driver, 10)
driver.find_element_by_css_selector("#autocomplete:nth-child(2)").send_keys("ind")
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "#ui-id-1 li")))
countryList = driver.find_elements_by_css_selector("#ui-id-1 li")
for country in countryList:
    if country.text == "India":
        country.click()
        break
# static dropdown
Dd = Select(driver.find_element_by_id("dropdown-class-example"))
Dd.select_by_index(2)
# checkbox
checkValues = driver.find_elements_by_xpath(
    "//legend[text()='Checkbox Example']/following-sibling::label/input[@type='checkbox']")
for checklists in checkValues:
    checklists.click()

# switch window
driver.find_element_by_id("openwindow").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.switch_to.window(driver.window_handles[0])
print("Switching window" + driver.title)

# switch tab
driver.find_element_by_id("opentab").click()
driver.switch_to.window(driver.window_handles[-1])
print(driver.title)

# switch alerts
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_id("alertbtn").click()
driver.switch_to.alert.accept()
driver.find_element_by_id("confirmbtn").click()
time.sleep(3)
driver.switch_to.alert.dismiss()

# table example get count of the number of rows
driver.find_elements_by_css_selector("table[name='courses'] tr")
a = len(driver.find_elements_by_css_selector("table[name='courses'] tr"))
b = a - 1
print("{} {}".format("Table data count is", b))
summation = 0

for x in range(2, 12, 1):
    course = "table[name='courses'] tbody tr:nth-child({0}) td:nth-child(2)".format(x)
    price = "table[name='courses'] tbody tr:nth-child({0}) td:nth-child(3)".format(x)
    courseName = driver.find_element_by_css_selector(course)
    PriceAmount = driver.find_element_by_css_selector(price)
    summation = summation + int(PriceAmount.text)
    print(courseName.text + " "+PriceAmount.text)

print(summation)

driver.quit()
