from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
 we should add all the Xpaths in variable or can maintain a file from where we can fetch them and use so that it will
 dynamic
'''

print("testing started")
# initialisse the Browser and launch the website
driver = webdriver.Chrome()
driver.get("https://www.easemytrip.com/hotels/")
driver.maximize_window()

# input new york and wait for suggestions and selecting the first opt
driver.find_element(By.CLASS_NAME,"hp_city").click()
driver.find_element(By.ID,"txtCity").send_keys("NewYork")
x=driver.find_elements(By.XPATH,"//ul[@id=\'ui-id-1\']/li")
wait = WebDriverWait(driver, 30)

element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='auto_sugg_tttl']")))
element.click()
# selecting the date from the drop down
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-handler='selectMonth']")))

element = wait.until(EC.presence_of_element_located((By.ID, "exithotelroom")))

# selecting the year from the drop down
select = Select(driver.find_element(By.XPATH,"//*[@data-handler='selectMonth']"))
select.select_by_visible_text('Jun')
select = Select(driver.find_element(By.XPATH,"//*[@data-handler='selectYear']"))
select.select_by_visible_text('2025')

element=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/div/table/tbody/tr/td/a")
for date in elements:
    if date.text == "10":
        date.click()
        break
elements=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/div/table/tbody/tr/td/a")
for date in elements:
    if date.text == "15":
        date.click()
        break

element = wait.until(EC.presence_of_element_located((By.ID, "exithotelroom")))
element.click()
driver.find_element(By.ID,"btnSearch").click()



original_window = driver.current_window_handle

element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='viewBtn']")))
element.click()

# Handling the multipple tabs
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Book Now']")))
element.click()

# enter the promo code
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sidebar']//input[@placeholder='Enter promo code']")))
element.send_keys("SUMMER25")
driver.find_element(By.XPATH,"//*[@id='sidebar']//span[text()='Apply']").click()

element= driver.find_element(By.XPATH,"//button[text()='Continue Booking']")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

'''
similar to the above text fields we can enter the test data in the customer input fields and click on contiue
'''

print("Testing Ended")
