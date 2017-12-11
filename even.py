#!/usr/bin/python3
def check_even(num):
    if num%2==0:
        print('{} is even.'.format(num))

    else:
        print('{} is odd.'.format(num))


num=int(input('Enter a number: '))

check_even(num)

