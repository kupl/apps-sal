# cook your dish here
T = int(input())

for t in range(T):
 n = 1
 b = 0
 l = 0
 llimit, blimit = input().split()
 blimit = int(blimit)
 llimit = int(llimit)
 
 while True:
  if n % 2 == 0:
   if b + n <= blimit:
    b += n
    n += 1
   else:
    print("Limak")
    break
  else:
   if l + n <= llimit:
    l += n
    n += 1
   else:
    print("Bob")
    break

