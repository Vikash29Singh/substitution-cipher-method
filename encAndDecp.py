# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:06:50 2019

@author: vikash
"""
from secret import secracy
key=secracy()

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext:
        try:
            i = (key.index(l) + n) % 81
            result += key[i]
            
        except ValueError:
            result += l

    return result

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 81
            result += key[i]
        except ValueError:
            result += l

    return result

text = input("Enter text : ")
offset = int(input("Enter private key : "))
if(offset == 0):
    while True:
        print("Enter value greater than 0")
        offset = int(input("Enter private key : "))
        if(offset != 0):
            break

    
encrypted = encrypt(offset, text)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEncrypted Message:', encrypted)
offsetNew = int(input("Enter private key : "))
if(offset == offsetNew):
    decrypted = decrypt(offset, encrypted)
    print('\nDecrypted Message:', decrypted)
else:
    print('\n                     Unauthorized access !\n                     !!! Access denied !!!')
    

