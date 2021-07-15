n = int(input())

a = [0] * 7

for i in range(n):
    s = input()
    for j in range(7):
        a[j] += ord(s[j]) - ord('0')

print(max(a))

