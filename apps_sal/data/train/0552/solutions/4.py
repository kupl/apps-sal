# cook your dish here
t = int(input())
for _ in range(t):
 n,k = map(int,input().split())
 carryBag = list(map(int,input().split()))
 carryBag.sort()
 w1 = min(k,n-k)
 son = sum(carryBag[:w1])
 father = sum(carryBag[w1:])
 print(father-son)
