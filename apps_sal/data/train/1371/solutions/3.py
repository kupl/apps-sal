# cook your dish here
try:
 for _ in range(int(input())):
  N, K = map(int, input().split())
  K = K % 7
  memory = list(map(int, input().split()))
  memory = list(map(lambda x: x + K, memory))
  memory = list(map(lambda x: x % 7, memory))
  print(memory.count(0))
except:
 pass
