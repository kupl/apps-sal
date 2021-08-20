mod = 8589934592
list1 = []
for i in range(int(input())):
    x = int(input())
    ans = (pow(2, x, mod) - 1) % mod
    list1.append((i + 1, ans))
for i in list1:
    print(f'Case {i[0]}: {i[1]}')
