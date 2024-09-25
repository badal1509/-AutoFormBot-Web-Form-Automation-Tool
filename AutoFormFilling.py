from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://forms.office.com/pages/responsepage.aspx?id=Dn_YOpMfvUGU9ILDfZcciHpTBLY2JshNuh6n299MCIFUOTM2N0hCODlYQzZFQlVXMTdFSzlSTFJFNy4u")

try:
    inputs = driver.find_elements(By.XPATH, "//input[@data-automation-id='textInput']")
    sleep(1)
    inputs[0].send_keys("Badal")
    sleep(1)
    inputs[1].send_keys("Singh")
    sleep(1)
    inputs[2].send_keys("Kushwaha")
    sleep(1)
    inputs[3].send_keys("Student")
    sleep(1)
    inputs[4].send_keys("M.J.R.P.Public School")
    sleep(1)
    inputs[5].send_keys("76")
    sleep(1)
    inputs[6].send_keys("CBSE")
    sleep(1)
    inputs[7].send_keys("M.J.R.P.Public School")
    sleep(1)
    inputs[8].send_keys("58")
    sleep(1)
    inputs[9].send_keys("CBSE")
    sleep(1)
    radio_button_male1 = driver.find_element(By.CSS_SELECTOR, "input[value='graduate']")
    radio_button_male1.click()
    sleep(1)
    radio_button_male2 = driver.find_element(By.CSS_SELECTOR, "input[value='BCA']")
    radio_button_male2.click()
    sleep(1)
    radio_button_male3 = driver.find_element(By.CSS_SELECTOR, "input[value='MCA']")
    radio_button_male3.click()
    sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, "[data-automation-id='submitButton']")
    submit_button.click()
    sleep(1)
except Exception as e:
    print(f"Error: {e}")

finally:
    input("Press Enter to close the browser...")
    driver.quit()