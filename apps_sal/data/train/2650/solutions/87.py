n, l = map(int, input().split())
lst = []
for i in range(n):
    s = input()
    lst.append(s)
lst = sorted(lst)
print(''.join(lst))
