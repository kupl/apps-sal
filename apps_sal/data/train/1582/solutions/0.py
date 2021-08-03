# cook your dish here
n = int(input())
s = [i for i in input()]
count = 0
for i in range(1, n):
    if s[i] == s[i - 1]:
        count += 1
    else:
        continue
print(count)
