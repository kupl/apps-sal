for _ in range(int(input())):
 n = int(input())
 s =0
 for _ in range(n):
  p,q,d=map(int,input().split())
  pi= p + (d/100 *p)
  p_new = pi -(d/100 * pi)
  loss = (p - p_new)*q
  s=s+(loss)
 print(s)
