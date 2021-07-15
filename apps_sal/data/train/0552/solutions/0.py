def main():
 T = int(input())
 for t in range(T):
  N,K = map(int, input().split())
  W = list(map(int, input().split()))
  W.sort()
  if 2*K > N:
   K = N - K
  kid = sum(W[:K])
  dad = sum(W[K:])

  diff = dad - kid

  print(diff)


def __starting_point():
 main()
__starting_point()
