'''Hashing exercise code template

Author: Beka Beriashvili

'''

#!/usr/bin/env python3

import random


def hash_remainder(key: int, size: int):
    '''Find hash using remainder'''
    return key%size

def hash_mid_sqr(key, size):
    '''Find hash using mid-square method'''
    h = str(key**2)
    if len(h) ==3:
        return int(h[0:2]) % size
    else:
        return int(h[1:3]) % size


def hash_folding(key: int, size: int):
    '''Find hash using folding method'''
    key = str(key)
    key = key.replace("-", "")
    h = 0
    for ch in range(0, len(key), 2):
        h += int(key[ch:ch+2])
    return h % size

    

def hash_str(key: str, size: int):
    '''Find string hash using simple sum-of-values method'''
    sum = 0
    key = str(key)
    for pos in range(len(key)):
        sum = sum + ord(key[pos])

    return sum%size

def hash_str_weighted(key: str, size: int):
    '''Find string hash using character positions as weights'''
    sum = 0
    key = str(key)
    for pos in range(len(key)):
        baba = ord(key[pos]) * pos
        sum = sum + baba

    return sum%size


def main():
    '''Main function'''
    keys_int = [10, 21, 32, 18, 17, 19, 42, 23, 99]
    keys_int_2 = [54, 26, 93, 17, 77, 31]
    keys_intstr = ['563-555-1234', '800-555-8080', '888-555-0000']
    keys_intstr_2 = ['436-555-4601']
    keys_str = ['pavel', 'bruce', 'talia', 'harvey', 'jim', 'alfred', 'lucius', 'jonathan', 'bane']
    keys_str_2 = ['algorithm', 'logarithm']

    print('Simple remainder')
    print([hash_remainder(x, 16) for x in keys_int])
    print([hash_remainder(x, 11) for x in keys_int_2])

    print('Mid-square')
    print([hash_mid_sqr(x, 16) for x in keys_int])
    print([hash_mid_sqr(x, 11) for x in keys_int_2])

    print('Folding')
    print([hash_folding(x, 16) for x in keys_intstr])
    print([hash_folding(x, 11) for x in keys_intstr_2])

    print('String hashing')
    print([hash_str(x, 16) for x in keys_str])
    print([hash_str(x, 11) for x in keys_str_2])

    print('Weighted string hashing')
    print([hash_str_weighted(x, 16) for x in keys_str])
    print([hash_str_weighted(x, 11) for x in keys_str_2])


if __name__ == '__main__':
    main()
