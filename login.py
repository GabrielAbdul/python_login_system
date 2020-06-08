#!/usr/bin/env python3
"""A python user login system"""


import json

def login():
	"""Function that will parse file containing user data and verify login credentials"""
	user_name = input("Username: ")
	user_pass = input("Password: ")

	try:
		with open("credentials.txt", 'r') as credentials:
			user_cred = json.loads(credentials.readline())
			if user_cred['user_name'] == user_name:
				if user_cred['user_password'] == user_pass:
						print("SUCCESS")
				elif user_cred['user_password'] != user_pass:
					print("INVALID PASS")
			if user_cred['user_name'] != user_name:
				print("invalid user name")
	except FileNotFoundError:
		print("File Not Found")

