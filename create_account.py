#!/usr/bin/env python3


import json

"""Module is used to create an account"""


def create_account():
	"""Function to create an account"""
	user_email = input("What is your email?\n")
	user_name = input("What is your user name?\n")
	user_password = input("What is your password?\n")

	user_info = {
		"user_email": user_email,
		"user_name": user_name,
		"user_password": user_password
	}

	try:
		with open("credentials.txt", 'x') as credentials:
			credentials.write("{}\n".format(json.dumps(user_info)))
	except FileExistsError:
		with open("credentials.txt", 'a') as credentials:
			credentials.write("{}\n".format(json.dumps(user_info)))
