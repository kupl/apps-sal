
def main():
 from sys import stdin,stdout
 Mod=10**9+7
 t=int(stdin.readline())
 for i in range(t):
  n,k=list(map(int,stdin.readline().split()))
  a=(k-1)%(n-1)
  d=n-1
  num=(k-1)//(n-1)+1
  res=(num*(2*a+(num-1)*d))//2
  stdout.write(str(res%Mod)+"\n")
 
def __starting_point():
 main()
__starting_point()
