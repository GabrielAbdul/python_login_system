#!/usr/bin/env python3
"""Login Module"""


import json

def login():
    """Function that will parse file containing user data and verify login credentials"""
    user_name = input("Username: ")
    if user_name == "":
        print("Must enter user name")
        return
    user_pass = input("Password: ")
    if user_pass == "":
        print("Must enter password")
        return

    try:
        with open("credentials.txt", 'r') as credentials:
            lines = credentials.readlines()
            for line in lines:
                user_cred = json.loads(line)
                if user_cred['user_name'] == user_name:
                    if user_cred['user_password'] == user_pass:
                        print("SUCCESS")
                        break
                    elif user_cred['user_password'] != user_pass:
                        print("INVALID PASS")
                if user_cred['user_name'] != user_name:
                    print("invalid user name")
    except FileNotFoundError:
        print("File Not Found")
