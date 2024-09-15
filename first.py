from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service = Service(executable_path=ChromeDriverManager().install()) 

useragent = UserAgent()
ua = useragent.random
opt = Options()
opt.add_argument(f'--user-agent={ua}')
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=service, options=opt)
actions = ActionChains(driver)


def parser() -> None:
    try:
        driver.get('https://www.nseindia.com/')
        market_data=WebDriverWait(driver=driver, timeout=2).until(expected_conditions.presence_of_element_located((By.ID, 'link_2')))
        actions.move_to_element(market_data).perform()
        time.sleep(2)
        url = '/market-data/pre-open-market-cm-and-emerge-market'
        pre_open=WebDriverWait(driver=driver, timeout=2).until(expected_conditions.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))
        actions.click(pre_open).perform()
        time.sleep(2)
        table = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, '//tbody')))
        with open('result.txt', 'w') as file:
            file.write(table.text)
        with open('parser_data.csv', 'w') as data, open('result.txt', 'r') as file:
            writer = csv.writer(data)
            writer.writerow(('name', 'prise'))
            read = file.readlines()
            for rows in read:
                list_row = rows.split(' ')
                writer.writerow((list_row[0], list_row[1]))
        url = "/market-data/new-stock-exchange-listings-today"
        step = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, f'//a[@href="'+url+'"]')))
        actions.click(step).perform()
        step = WebDriverWait(driver=driver, timeout=3).until(expected_conditions.presence_of_element_located((By.XPATH, '//button[@aria-label="Pre Open Book - REVATHIEQU"]')))
        actions.click(step).perform()
        time.sleep(5)
        driver.execute_script('window.scrollBy(0, 500)')
        time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    parser()