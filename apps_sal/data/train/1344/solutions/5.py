# cook your dish here
n = int(input())
for i in range(n):
 num = int(input())
 lis = list(map(int,input().split()))
 mini = min(lis)
 lis.remove(mini)
 mini2 = min(lis)
 print(mini + mini2)
