# cook your dish here
"""
Created on Sat May 23 22:56:03 2020

@author: aurouS_EeRiE
"""


for _ in range(int(input())):
    vowel = ['a', 'e', 'i', 'o', 'u']
    s = input()
    temp = ""
    for i in s:
        if i in vowel:
            temp += '0'
        elif i.isalpha():
            temp += '1'
    print(int(temp, 2) % ((10 ** 9) + 7))
