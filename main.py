from time import sleep
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def main():
    server_url = "http://127.0.0.1:4723"

    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'ZY22DHFVBM'
    options.app = "/path/to/your/app.apk"
    
    driver = webdriver.Remote(command_executor=server_url, options=options)
    
    sleep(5)
    driver.find_element(by= AppiumBy.ID, value= 'com.app_test:id/identity_landing_social_button_text').click()
    sleep(3)
    driver.find_element(by= AppiumBy.ID, value= 'com.app_test:id/identity_text_input_edit_text').click()
    sleep(3)
    driver.hide_keyboard()
    sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/identity_text_input_edit_text').send_keys("uni.ramos.telecomun@gmail.com")
    sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/identity_landing_social_button').click()
    sleep(10)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/identity_landing_social_button').click()
    sleep(12)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/genius_onbaording_bottomsheet_cta').click()
    sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/facet_search_box_basic_field_label').click()
    sleep(3)
    driver.hide_keyboard()
    sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/facet_with_bui_free_search_app_test_header_toolbar_content').send_keys("cuzco")
    sleep(3)
    driver.find_element(by=AppiumBy.ID, value='com.app_test:id/facet_disambiguation_content', index=0)
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
