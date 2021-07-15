def main():
 for i in range(int(input())):
  n, p = list(map(int,input().split()))
  m = n%(n//2 + 1)
  if m==0:
   print(p*p*p)
  else:
   c1 = p-n
   t1 = c1*c1
   t2 = c1*(p-m)
   t3 = (p-m)*(p-m)
   cases = t1+t2+t3
   print(cases)

main()



