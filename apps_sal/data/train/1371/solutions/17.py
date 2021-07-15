def __starting_point():
 for i in range(int(input())):
  N, K = map(int,input().split())
  count=0
  N = list(map(int,input().split()))
  print(sum([True for x in N if (K+x)%7==0]))
__starting_point()
