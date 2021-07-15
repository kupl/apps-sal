# cook your dish here
t = int(input())

for i in range(t):
 n = int(input())

 array = list(map(int, input().split()))

 minEle = min(array)
 print(minEle * (n - 1))
