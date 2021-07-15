# cook your dish here
n = int(input())
while n>0:
    s = input()
    print(int(s[0])+int(s[(len(s)-1)]))
    n = n-1
