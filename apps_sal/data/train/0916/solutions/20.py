def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x
def cm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    print(cm(n,m))

