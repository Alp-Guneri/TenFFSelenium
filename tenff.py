from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from driver import initialize_default_driver


def tenff_automate(driver):
    driver.get("https://10fastfingers.com/typing-test/english")
    handle_cookies_and_ads(driver)
    play_once(driver)


def handle_cookies_and_ads(driver):
    try:
        wait_reject_cookies_button = WebDriverWait(driver, timeout=5)

        # Reject Cookies
        wait_reject_cookies_button.until(presence_of_element_located((By.CSS_SELECTOR,
                                                                      "#CybotCookiebotDialogBodyButtonDecline")))
        deny_cookies_button = driver.find_element(by=By.CSS_SELECTOR, value="#CybotCookiebotDialogBodyButtonDecline")
        deny_cookies_button.click()
        print("Cookies rejected!")

        # Close Ads
        # wait.until(presence_of_element_located((By.CSS_SELECTOR, "#closeIconHit")))
        close_ad_button = driver.find_element(by=By.CSS_SELECTOR, value="#closeIconHit")
        close_ad_button.click()
        print("Ad closed!")
    except Exception:
        print("No ads/cookie window found")

def play_once(driver):
    # Wait until we have the div containing the words
    wait = WebDriverWait(driver, timeout=5)
    wait.until(presence_of_element_located((By.CSS_SELECTOR, "#row1")))

    # Get the words list
    word_spans = driver.find_elements(by=By.CSS_SELECTOR, value="#row1 > span")

    words = []
    for span in word_spans:
        words.append(span.get_attribute("textContent"))

    # Find the input field
    text_input_element = driver.find_element(by=By.CSS_SELECTOR, value="#inputfield")
    text_input_element.click()

    action_chain = ActionChains(driver)
    for i in range(len(words) - 1):
        word = words[i]
        action_chain.send_keys(word).perform()
        action_chain.send_keys(Keys.SPACE).perform()


def play_again(driver):
    replay_button = driver.find_element(by=By.CSS_SELECTOR, value="#reload-btn")
    replay_button.click()


def element_located_has_non_empty_text(locator):
    def _predicate(driver):
        try:
            element = driver.find_element(*locator)
            return len(element.text) > 0
        except StaleElementReferenceException:
            print("element not found!")
            return False

    return _predicate
