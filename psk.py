#!/usr/bin/python3
global psk
psk='anuska613'

def check_psk():
    passwd=input('Enter the password: ')
    
    if psk==passwd:
        print('Password match.')
    else:
        print('Wrong password.')


check_psk()
