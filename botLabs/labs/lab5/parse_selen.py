from selenium import webdriver
from selenium.webdriver.common.by import By

def get_exchange_rates():
    driver = webdriver.Chrome()
    driver.get("https://cbr.ru/currency_base/daily/")

    title = driver.title
    sect = driver.find_element(By.XPATH, "//h2[@class='h3']").text
    table = driver.find_element(By.XPATH, "//table[@class='data']").text

    print(title)
    print(sect)
    print(table)

    driver.close()
    return title, sect, table


if __name__ == '__main__':
    get_exchange_rates()
