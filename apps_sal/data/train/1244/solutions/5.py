n = int(input())
list1 = []
for i in range(n):
    (b, d) = list(map(int, input().strip().split()))
    if b >= 0 and d <= 0 or (b <= 0 and d >= 0):
        s = abs(b) + abs(d) + 1
        list1.append(s)
    else:
        s = abs(abs(b) - abs(d)) + 1
        list1.append(s)
s = sum(list1)
print(s % 1000000007)
