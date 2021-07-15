def main():
 t = int(input())
 a_c = "Chefirnemo"
 a_n = "Pofik"
 while t:
  t -= 1
  n, m, x, y = list(map(int, input().split()))
  res = a_n
  
  if ( (n-1)%x==0) and ( (m-1)%y==0 ):
   res=a_c
  if (n-2)%x == 0 and n >= 2 and (m-2)%y == 0 and m >= 2:
   res = a_c
  print(res)

try:
 main()
except:
 pass
