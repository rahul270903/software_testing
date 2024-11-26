from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GoogleForm:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def fill_form(self):
        try:
            self.driver.get("https://docs.google.com/forms/u/0/?pli=1&tgif=d")
            time.sleep(2)

            name_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            name_input.send_keys("Prabhu Deva")

            age_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            age_input.send_keys("25")

            email_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            email_input.send_keys("yogeshs.is21@sahyadri.edu.in")

            country_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            country_input.send_keys("India")

            city_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            city_input.send_keys("Chennai")

            area_input = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            area_input.send_keys("Teynampet")

            submit = self.driver.find_element(By.XPATH, '//*[@id="mG6Hd"]/div[2]/div/div[2]/div[7]/div/div')
            submit.click()
            time.sleep(2)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
    automation = GoogleForm()
    automation.fill_form()
    automation.tear_down()