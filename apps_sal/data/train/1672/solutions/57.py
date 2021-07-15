s=[int(input()) for i in range(1,12)][::-1]
for i in range(11):
  a=s[i]
  a=(a if a>0 else -a)**.5
  b=(s[i]**3)*5
  r=a+b

  if r>400:
    print("f({}) = MAGNA NIMIS!".format(s[i]))
  else:
    print("f({}) = {:.2f}".format(s[i],r))    

