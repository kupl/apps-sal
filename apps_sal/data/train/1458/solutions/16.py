t = int(input())
while t :
 n = int(input())
 count = 0
 for i in range(1 , n + 1 , 2 ) :
  count = count + ((n + 1 - i) * (n + 1 -i))
 print(count)
 t = t-1

