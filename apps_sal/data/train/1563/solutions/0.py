n = int(input())
for index in range(0, n):
 a, b = list(map(str, input().split()))
 a = int(a[::-1])
 b = int(b[::-1])
 a = str(a + b)
 a = int(a[::-1])
 print(a)
