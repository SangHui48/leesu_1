from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    url = 'https://www.google.com'
    driver.get(url)



if __name__ == "__main__":
    main()