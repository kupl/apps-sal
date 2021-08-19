# cook your dish here
n = int(input())
for i in range(n):
    s = input().split(" ")
    s[0] = int(s[0])
    s[1] = int(s[1])
    print(s[0] + s[1] - 1)
