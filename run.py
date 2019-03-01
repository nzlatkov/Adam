from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

url = 'https://www.messenger.com'
email = None
password = None

chat_id = None
invoke = '!adam '
answered_messages = []

browser = webdriver.Chrome('chromedriver.exe')
browser.get(url)

def login():
	email_box = browser.find_element_by_name('email')
	password_box = browser.find_element_by_name('pass')
	login_button = browser.find_element_by_name('login')

	time.sleep(3)
	email_box.send_keys(Keys.TAB)

	email_box.send_keys(email)
	password_box.send_keys(password)
	login_button.click()


def connect_to_chat():
	browser.get('https://www.messenger.com/t/' + chat_id)
	time.sleep(4)


def check_for_invoke():
	messages = browser.find_elements_by_class_name('_58nk')
	messages = [message.text for message in messages]

	for message in reversed(messages):
		if message[:len(invoke)] == invoke and message[len(invoke):] not in answered_messages:
			answered_messages.append(message[len(invoke):])
			return message[len(invoke):]

	return None


def send_message(message):
	textbox = browser.find_element_by_class_name('_5rpu')
	textbox.send_keys(message)
	textbox.send_keys(Keys.ENTER)


if __name__ == '__main__':
	email = sys.argv[1]
	password = sys.argv[2]
	chat_id = sys.argv[3]

	while True:
		try:
			login()
			connect_to_chat()
			break
		except:
			time.sleep(3)
			browser.get(url)

	while True:
		message = check_for_invoke()
		
		if message is not None:
			print(message)
			send_message('Hello World')
