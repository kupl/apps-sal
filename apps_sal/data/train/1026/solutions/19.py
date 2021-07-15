test = int(input())
for _ in range(test):
 array = list(map(int, input().split()))
 array.sort()
 mod = 1000000007
 answer = (array[0])*((array[1]-1))*((array[2]-2))
 if answer<=0:
  print(0)
 else:
  print(answer%mod)
