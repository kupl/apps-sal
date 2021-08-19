# cook your dish here
t = int(input())

for i in range(t):
    lst = list(map(int, input().split()))
    print(lst[3] - lst[1], lst[3] - lst[2], lst[3] - lst[0])
