#!/usr/bin/env python3


from login import login
from create_account import create_account as create
"""Module that asks user to login or create an account"""

user_input = input("To Login press ENTER.\nTo create an account enter C\n")

if type(user_input) is not str and user_input is not "":
	raise TypeError("Must be a string")

if user_input == '':
	login()
elif user_input == 'C' or user_input == 'c':
	create()

