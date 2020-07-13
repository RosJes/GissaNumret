import random
import re
'''step 1: generate an array of chars without conditions'''
'''step 2: add conditions to array of chars'''

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
password_length=input('Password length?')
converted_length=int(password_length)
allow_upper=input('Allow uppercase?')
allow_lower=input('Allow lowercase?')
allow_numbers=input('Allow numbers?')
allow_spec_char=input('Allow special character?')
password=''
for x in range(converted_length):
    if allow_lower == 'n':
        x = re.findall("[A-Z\d @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)
    if allow_upper == 'n':
        x = re.findall("[a-z\d @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)
    if allow_numbers == 'n':
        x = re.findall("[a-z @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)
    if allow_spec_char == 'n':
        x = re.findall("[A-z\d ]", chars)
        password += random.choice(x)

'''Reg Ex check: upper, lower osv'''
'''fix logical problem with correct if statements'''

print(f'Your generated password is: {password}')

