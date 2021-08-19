s = input()
s = s.split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
n = int(input())
s = input()
s = s.split()
count = 0
for i in range(n):
    if int(s[i]) > b and int(s[i]) < c:
        count += 1
print(count)
