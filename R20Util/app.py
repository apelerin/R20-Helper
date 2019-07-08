from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import functions


# Function to connect on Roll20 then launch a game
def login_and_launch_game():
	user = input("Mail: ")
	pwd = input("Password: ")
	driver = webdriver.Firefox()
	driver.get("https://app.roll20.net/editor/")
	assert "Roll20" in driver.title
	user_input = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/form/input[1]")
	user_input.send_keys(user)
	password_input = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/form/input[2]")
	password_input.send_keys(pwd)
	login_btn = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/form/p[2]/button")
	login_btn.click()
	driver.implicitly_wait(15)
	driver.get(input("Game Link"))
	driver.implicitly_wait(20)
	return driver


# Listen to the chat inside the game
def listining_to_chat(driver):
	previous_id = 'None'
	while 1:
		# Searching for the last message in chat, then check if it already process it
		last_message = driver.find_elements_by_class_name('message')[-1]
		if last_message.get_attribute('data-messageid') != previous_id:
			if last_message.text.startswith('peutchon'):
				# Search for the right function to apply
				functions.switcher(last_message.text, driver)
			previous_id = last_message.get_attribute('data-messageid')

driver = login_and_launch_game()
listining_to_chat(driver)
