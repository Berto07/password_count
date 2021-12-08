#!/usr/bin/env python 

username = input('what is your username ')
password = input('what is your password? ')

hidden_password = '*' * len(password)

print(f'{username}, your password, {hidden_password}, is {len(password)} letters long')