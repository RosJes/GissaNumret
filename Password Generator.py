import random
'''step 1: generate an array of chars without conditions'''
'''step 2: add conditions to array of chars'''

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
password_length=input('Password length?')
converted_length=int(password_length)
password=''
for x in range(converted_length):
    password += random.choice(chars)

print(password)

