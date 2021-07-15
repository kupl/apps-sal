a = input()
b = input()
cnt1 = a.count('1') + (a.count('1') % 2 == 1)
cnt2 = b.count('1')
print('YES'if cnt1 >= cnt2 else'NO')

