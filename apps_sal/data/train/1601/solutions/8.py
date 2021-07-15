from sys import stdin

t = int(stdin.readline())

while t:
 n, p = [int(x) for x in stdin.readline().split()]

 l_rem = n % ((n//2) + 1)
 
 if l_rem == 0:
  print(p*p*p)
 else:
  ans = (p-l_rem)*(p-l_rem)
  ans += (p-n)*(p-l_rem)
  ans += (p-n)*(p-n)
  print(ans)

 t -= 1
