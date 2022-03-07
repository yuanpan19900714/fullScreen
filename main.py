from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    global driver
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('--kiosk')
    edge_options.page_load_strategy = 'normal'
    edge_options.add_experimental_option('useAutomationExtension', False)
    edge_options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
    driver = webdriver.Edge(executable_path='msedgedriver', options=edge_options)
    driver.get('http:localhost:80')
    # driver.find_element(By.ID, 'fullScreen').click()
    # driver.maximize_window()
    # Keys.F11
