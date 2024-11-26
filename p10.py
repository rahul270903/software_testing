from selenium import webdriver
import time

class webPageFetcher:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def fetch_page(self):
        try:
            self.driver.get("https://www.btreesystems.com/selenium-with-python-training-in-chennai/")

           
            time.sleep(180)

            page_source = self.driver.page_source.encode('utf-8')
            with open('result.html', 'wb') as f:
                f.write(page_source)
            print("Page fetched successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    fetcher = webPageFetcher()
    fetcher.fetch_page()
    fetcher.tear_down()