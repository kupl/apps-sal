"""
Created on Sat May 23 22:12:36 2020

Title: Value of Name

Contest: LockDown Test 4.0 

@author: mr._white_hat_
"""
for _ in range(int(input())):
    T = input()
    S = ''
    for i in T:
        if i in ('a', 'e', 'i', 'o', 'u'):
            S += '0'
        elif i.isalpha():
            S += '1'
    print(int(S, 2) % 1000000007)
