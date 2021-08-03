"""
Brandt Smith, Lemuel Gorion and Peter Haddad

codeforces.com

Problem 878A
"""
a, b = 0, 1023

n = int(input())

for i in range(n):
    l, r = input().split(' ')
    r = int(r)

    if l == '|':
        a, b = a | r, b | r
    elif l == '&':
        a, b = a & r, b & r
    elif l == '^':
        a, b = a ^ r, b ^ r

print('3')
print('&', (1023 & a) | b)
print('^', a & (1023 ^ b))
print('|', a & b)
