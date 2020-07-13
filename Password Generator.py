import random
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
    password += random.choice(chars)
    '''Reg Ex check: upper, lower osv'''

print(f'Your generated password is: {password}')

