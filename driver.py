from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def initialize_default_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver


def initialize_sneaky_driver():
    data_dir = "C:/Users/ealpg/AppData/Local/Google/Chrome/User Data/Profile 5"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    return driver
