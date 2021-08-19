s = input()
dp = [1, 1]
cant = False
if 'c' in s or 'k' in s:
    cant = True
for i in range(1, len(s)):
    if s[i] + s[i - 1] == 'gg' or s[i] + s[i - 1] == 'ff':
        dp.append(dp[-1] + dp[-2])
    else:
        dp.append(dp[-1])
if cant:
    print(0)
else:
    print(dp[-1] % (10 ** 9 + 7))
