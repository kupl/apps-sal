def main():
 T = int(input())
 for i in range(T):
  N = int(input())
  S = input()
  R = {}
  for i in range(N):
   if S[i] == '1':
    R[i-1] = 2
    R[i] = 2
    R[i+1] = 2
  R[-1] = 0
  R[N] = 0
  print(N - list(R.values()).count(2))



def __starting_point():
 main()



__starting_point()
