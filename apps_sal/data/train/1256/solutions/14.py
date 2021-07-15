import math
test = int(input())
for _ in range(test):
 n=int(input())
 array =list(map(int, input().split()))
 count = n- array.count(1) - array.count(0) - array.count(2)
 print(count*(count-1)//2 + array.count(2)*count)
