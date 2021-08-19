"""
Created on ١٢\u200f/١٢\u200f/٢٠١٤

@author: mohamed265
"""
'\ns = input()\nn = len(s)\nslon = ""\nfor i in range(1, n):\n    if s[i] == \'0\' and s[i - 1] != \'0\':\n        t = s[0:i] + s[i + 1:n]\n        slon = max(slon, t)\nif len(slon) != n - 1:\n    slon = s[1:]\nprint(slon)\n\ns = input()\nn = len(s)\nslon = ""\nk = temp = 0\nfor i in range(1, n):\n    if s[i] == \'0\':\n        t = s[0:i] + s[i + 1:n]\n        k = int(t, 2)\n        print(t , k)\n        if k > temp:\n            temp = k\n            slon = t\nif len(slon) != n-1:\n    slon = s[1:]\nprint(slon)\n'
s = input()
temp = s.find('0')
print(s[1:]) if temp == -1 else print(s[0:temp] + s[temp + 1:])
