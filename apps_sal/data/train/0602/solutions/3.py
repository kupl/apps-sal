# cook your dish here
s = list(input().split())
a = min(s, key=len)
for i in s:
    print(a, i, end=" ")
print(a)
