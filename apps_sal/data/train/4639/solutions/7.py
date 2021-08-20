def power_of_two(x):
    if x == 0:
        return False
    elif x & x - 1 != 0:
        return False
    else:
        return True
    '\n    count = 0\n    while (x): \n        count += x & 1\n        x >>= 1\n    if count==1:\n        return True\n    else:\n        return False\n   \n    string = bin(x)[2:]\n    Sum=0\n    for x in range(len(string)):\n        if string[x]=="1":\n            Sum+=1\n    if Sum==1:\n         return True\n    else:\n          return False\n    '
