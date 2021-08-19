# cook your dish here
x = int(input())
for i in range(x):
    lst = [int(item) for item in input().split()]
    lst.sort()
    print(lst[-2])
