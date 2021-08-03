from sys import stdin, stdout
n = int(input())
a = []
count1 = 0
count2 = 0
for i in range(n):
    a.append(int(stdin.readline()))
a.sort()
while count2 != n // 2:
    if a[count1] * 2 <= a[count2 + n // 2]:
        count1 += 1
        count2 += 1
    else:
        count2 += 1
stdout.write(str(n - count1))
