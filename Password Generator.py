import random
import re
'''step 1: generate an array of chars without conditions'''
'''step 2: add conditions to array of chars'''
'''remeber to filter out a correkt password from if statements'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
password_length=input('Password length?')
converted_length=int(password_length)
password=''
stringbuilder=''
allow_upper=input('Allow uppercase?')
allow_lower=input('Allow lowercase?')
allow_numbers=input('Allow numbers?')
allow_special_char=input('Allow special character')
for x in range(converted_length):
        x = re.findall("[A-z\d @_!#$%^&*()<>?/\|}{~:]", chars)
        password += random.choice(x)

'''Reg Ex check: upper, lower osv'''
'''fix logical problem with correct if statements'''
'''make string builder filtered by the questions, then apply to regex method'''

print(f'Your generated password is: {password}')

