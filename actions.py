# actions.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from locators import Locators
from config import BASE_URL

class MumzworldAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Change to Firefox() if needed
        self.driver.maximize_window()

    def  opens_mumzworld_web_store(self):
        self.driver.get(BASE_URL)
        time.sleep(3)
        try:
            shadow_host = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Locators.POPUP_HOST))
            )

            for _ in range(3):
                try:
                    shadow_root = self.driver.execute_script("return arguments[0].shadowRoot;", shadow_host)
                    WebDriverWait(self.driver, 10).until(lambda d: shadow_root.find_element(By.ID, "close"))

                    popup_close_button = self.driver.execute_script(
                        "return document.querySelector(arguments[0]).shadowRoot.querySelector(arguments[1]);",
                        Locators.POPUP_HOST, Locators.POPUP_CLOSE
                    )
                    time.sleep(6)
                    self.driver.execute_script("arguments[0].click();", popup_close_button)
                    print("Popup closed successfully!")
                    self.driver.refresh()
                    return
                except Exception as inner_e:
                    print(f"Retrying due to stale element: {str(inner_e)}")

            pytest.fail("Popup could not be closed after multiple attempts.")

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, Locators.LOGO))
                )
                print("Home page loaded successfully with logo.")
                return True
            except Exception as e:
                print(f"Error finding element: {e}")
                return False

        except Exception as e:
            pytest.fail(f"Popup not found or could not be closed: {str(e)}")

    def search_a_product(self, phrase):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.SEARCH_BAR))
            )
            search_box.clear()
            search_box.send_keys(phrase)
            search_box.send_keys(Keys.ENTER)

            print(f"Search for '{phrase}' executed successfully.")
            time.sleep(5)

            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, Locators.SEARCH_RESULTS))
            )

            return True

        except Exception as e:
            print(f"Error searching for product: {e}")
            return False

    def add_products_to_bag(self):
        try:
            products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, Locators.SEARCH_RESULTS))
            )

            if not products:
                print("No products found!")
                return False

            first_product = products[0]
            print("Found first product:", first_product.text)

            add_to_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locators.ADD_TO_CART_BUTTON))
            )

            self.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
            self.driver.execute_script("arguments[0].click();", add_to_cart_button)

            print("Product added to cart successfully!")
            time.sleep(2)
            return True

        except Exception as e:
            print(f"Error adding product to cart: {e}")
            return False

    def go_to_view_bag(self):
        try:
            cart_btn = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, Locators.CART_BUTTON))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", cart_btn)
            cart_btn.click()
            time.sleep(4)
        except Exception as e:
            print(f"Error navigating to cart page: {e}")
            return False

    def update_the_qty(self):
        try:
            qty = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, Locators.QTY_INPUT))
            )
            qty.clear()
            qty.send_keys("5")
            time.sleep(6)
        except Exception as e:
            print(f"Error updating quantity: {e}")
            return False

    def click_proceed_to_checkout(self):
        try:
            proceed_to_checkout_btn = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, Locators.PROCEED_CHECKOUT_BUTTON))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", proceed_to_checkout_btn)
            proceed_to_checkout_btn.click()
            time.sleep(3)
        except Exception as e:
            print(f"Error proceeding to checkout: {e}")
            return False

    def register_a_new_user(self):
        try:
            create_acc = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, Locators.NAV_CREATE_ACCOUNT))
            )
            create_acc.click()
            print("Successfully navigated to the create account form page!")
            time.sleep(3)
            # Wait until the form is visible
            wait = WebDriverWait(self.driver, 10)
            form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

            # Fill out the form
            self.driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("TestByNoel")
            self.driver.find_element(By.XPATH, "//input[@id='lastname']").send_keys("TestByNoel")
            self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test01@gmail.com")
            self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("mumzworld@123")
            time.sleep(5)

            # Click the submit button
            self.driver.find_element(By.XPATH, "//button[@id='register_btn']").click()

            # Wait for the response (Optional)
            wait.until(EC.url_changes("https://www.mumzworld.com/en/create-account"))
            time.sleep(15)

            print("Successfully created an new account")
        except Exception as e:
            print(f"Error while registering a user: {e}")
            return False

    def close_browser(self):
        self.driver.quit()
