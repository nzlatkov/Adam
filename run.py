from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

url = 'https://www.messenger.com'
invoke = '!adam '

browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)

answered_messages = []

def login(email, password):
	email_box = browser.find_element_by_name('email')
	password_box = browser.find_element_by_name('pass')
	login_button = browser.find_element_by_name('login')

	time.sleep(3)
	email_box.send_keys(Keys.TAB)

	email_box.send_keys(email)
	password_box.send_keys(password)
	login_button.click()


def connect_to_chat(chat_id):
	browser.get('https://www.messenger.com/t/' + chat_id)
	time.sleep(4)


def check_for_invoke():
	message = browser.find_elements_by_class_name('_58nk')[-1].text

	if message[:len(invoke)] == invoke:
		return message[len(invoke):]
	else:
		return None


def send_message(message):
	textbox = browser.find_element_by_class_name('_5rpu')
	textbox.send_keys(message)
	textbox.send_keys(Keys.ENTER)


if __name__ == '__main__':
	# email = sys.argv[1]
	# password = sys.argv[2]
	# chat_id = sys.argv[3]
	email = 'adam_the_ai@abv.bg'
	password = 'marakesh1999'
	chat_id = '100008733464069'

	while True:
		try:
			login(email, password)
			connect_to_chat(chat_id)
			break
		except:
			time.sleep(3)
			browser.get(url)

	while True:
		message = check_for_invoke()
		
		if message is not None:
			print(message)
			send_message('Hello World')
