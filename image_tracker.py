from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options 

 

 

def main():
    # 브라우저 꺼짐 방지 옵션 
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://www.google.com'
    driver.get(url)


if __name__ == "__main__":
    main()