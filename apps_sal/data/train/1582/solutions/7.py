n = int(input())
s = input()
count = 0
for i in range(n):
    if(i + 1 == n):
        break
    if s[i] == s[i + 1]:
        count += 1
print(count)
