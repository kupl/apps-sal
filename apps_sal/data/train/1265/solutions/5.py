def str_base(number, base):
   (d,m) = divmod(number,len(base))
   if d > 0:
      return str_base(d,base)+base[m]
   return base[m]

for _ in range(int(eval(input()))):
	n = int(eval(input()))
	print(str_base(n-1,'02468')) 
