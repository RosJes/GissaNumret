import random
import re
'''step 1: generate an array of chars without conditions'''
'''step 2: add conditions to array of chars'''

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
password_length=input('Password length?')
converted_length=int(password_length)
password=''
allow_upper=input('Allow uppercase?')
allow_numbers=input('Allow numbers?')
for x in range(converted_length):
    if allow_upper=='y':
        x = re.findall("[A-z @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)
    else:
        x = re.findall("[a-z @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)

'''Reg Ex check: upper, lower osv'''
'''fix logical problem with correct if statements'''

print(f'Your generated password is: {password}')

