from src.testproject.sdk.drivers import webdriver


def test1():
    driver = webdriver.Chrome(token='xMOUq-CTwc12Ru7Vjls1syE6uZ8B7vxcv1KAs55XaOY1')

    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys("12345")
    driver.find_element_by_css_selector("#login").click()

    passed = driver.find_element_by_css_selector("#logout").is_displayed()

    print("Test passed") if passed else print("Test failed")

    driver.quit()


if __name__ == "__main__":
    test1()
