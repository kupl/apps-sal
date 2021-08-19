# cook your dish here
n = int(input())
l = list(map(int, input().split()[:n]))
print(max(l), min(l))
