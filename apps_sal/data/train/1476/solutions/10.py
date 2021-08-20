import math
for _ in range(int(input())):
    s = input()
    a = [0] * 26
    b = [0] * 26
    for i in range(len(s)):
        if s[i].islower():
            a[97 - ord(s[i])] += 1
        else:
            b[65 - ord(s[i])] += 1
    sum = math.factorial(len(s))
    su = sum
    for i in range(26):
        su = su // (math.factorial(a[i]) * math.factorial(b[i]))
    print(su % (10 ** 9 + 7))
