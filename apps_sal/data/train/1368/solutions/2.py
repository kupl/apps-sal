# cook your dish here
t = int(input())

for _ in range(t):
    height, thresh  = map(int,input().split())
    if height >= thresh:
        print("Yes")
    else:
        print("No")
