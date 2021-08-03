# cook your dish here
n = int(input())
l = [1, 2, 145, 40585]
for i in range(n):
    t = int(input())
    if t in l:
        print(1)
    else:
        print(0)
