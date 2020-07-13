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
if allow_lower=='y'and allow_upper=='y':
    stringbuilder = 'A-z'
elif allow_lower=='y'and allow_upper=='n':
    stringbuilder = 'a-z'
elif allow_lower=='n'and allow_upper=='n':
    stringbuilder = ' '
else:
    stringbuilder = 'A-Z'
allow_numbers=input('Allow numbers?')
if allow_numbers=='y':
    newstring=stringbuilder+'\d'
else:
    newstring=stringbuilder
allow_spec_char = input('Allow special char?')
if allow_spec_char=='y' and allow_numbers == 'y':
       newstring=stringbuilder + '\d'+'@_!#$%^&*()<>?/\|}{~:'
if allow_spec_char=='n' and allow_numbers == 'y':
       newstring=stringbuilder+'\d'
elif allow_spec_char == 'n':
        newstring=stringbuilder
else:
    stringbuilder
print(newstring)
for x in range(converted_length):
        x = re.findall(f'[{newstring}]', chars)
        password += random.choice(x)

'''Reg Ex check: upper, lower osv'''
'''fix logical problem with correct if statements'''
'''make string builder filtered by the questions, then apply to regex method'''

print(f'Your generated password is: {password}')

