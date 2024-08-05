from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest
import allure

# PyTest with Selenium and Integration with Jenkins and Allure Reporting
# 2
@pytest.fixture()
# 1
def test_setup():
    global driver
    driver      = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield
    driver.quit()
    
# 3
# Mendeskripsikan apa yang ingin di uji
@allure.description("Validation OrangeHRM with invalid username and valid password")
# Tingkat keparahan dari kasus uji 
@allure.severity(severity_level="CRITICAL")
# 3
def test_invalidusername(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("admin123")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')

    submit  =   driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    submit.click()
    sleep(2)
    # mengimplementasikan dari pytest
    try: 
        text    = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard"
    except:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential", attachment_type=allure.attachment_type.PNG)
    # 9
    # finally:
    #     pass

# 4
# Mendeskripsikan apa yang ingin di uji
@allure.description("Validation OrangeHRM with valid username and invalid password")
# Tingkat keparahan dari kasus uji 
@allure.severity(severity_level="CRITICAL")
# 4 
def test_invalidpassword(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("Admin")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('ad1234443')

    submit  =   driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    submit.click()
    sleep(2)
    # mengimplementasikan dari pytest
    try: 
        text    = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard"
    except:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential", attachment_type=allure.attachment_type.PNG)
    # 10
    # finally:
    #     pass

# 5 - FALSE
# Mendeskripsikan apa yang ingin di uji
@allure.description("Validation OrangeHRM with valid username and empty password")
# Tingkat keparahan dari kasus uji 
@allure.severity(severity_level="CRITICAL")
# 5 
def test_invalidusernameempty(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')

    submit  =   driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    submit.click()
    sleep(2)
    # mengimplementasikan dari pytest
    try: 
        text    = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard"
    except:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential", attachment_type=allure.attachment_type.PNG)
    # 12
    # finally:
        # pass 

# 6
# Mendeskripsikan apa yang ingin di uji
@allure.description("Validation OrangeHRM with valid login credential")
# Tingkat keparahan dari kasus uji 
@allure.severity(severity_level="NORMAL")
# 6 
def test_invalidpasswordempty(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").clear()
    enter_username("Admin")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    enter_password('')

    submit  =   driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    submit.click()
    sleep(2)
    # mengimplementasikan dari pytest
    try: 
        text    = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard"
    except:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential", attachment_type=allure.attachment_type.PNG)
    # 13
    # finally:
    #     pass

# 7
# Mendeskripsikan apa yang ingin di uji
@allure.description("Validation OrangeHRM with valid login credential")
# Tingkat keparahan dari kasus uji 
@allure.severity(severity_level="NORMAL")
# 7 
def test_validlogin(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.NAME, "username").clear()
    enter_username("Admin")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
    enter_password('admin123')

    submit  =   driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    submit.click()
    sleep(2)
    # mengimplementasikan dari pytest
    try: 
        text    = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert text == "Dashboard"
    # except:
    #     pass
    # 13
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credential", attachment_type=allure.attachment_type.PNG)

def test_teardown(test_setup):
    sleep(5)
    driver.quit()
    
# 8
# agar memudahkan penggunaan nya
@allure.step('Entering username as {0}')
def enter_username(username):
    driver.find_element(By.NAME, "username").send_keys(username)
    
@allure.step('Entering password as {0}')
def enter_password(password):
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

# python -m pytest test_login.py
# python -m pytest test_login.py --alluredir=reports