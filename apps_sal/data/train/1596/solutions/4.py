import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
 X,Y = list(map(int,input().split()))
 x = X+1
 y = Y +1
 def bit(x):
  a = []
  while x>0:
   a.append(x&1)
   x = x//2

  return sum(a)
 
 count_x = bit(x)
 count_y = bit(y)


 # while(x>0):
 #   n = bit(x)
 #   # print('n_x ' , n)
 #   if x == 2**(n+1)-1:
 #       count_x += 1
 #       break
 #   elif 2**n -1 < x:
 #       x = (x-(2**n-1))
 #       count_x +=1
 #       if x != 1:
 #           x = x-1
 #       else:
 #           count_x += 1
 #           break
   
 
 # while y>0:
 #   n = bit(y)
 #   # print('n ' , n)
 #   if y == 2**(n+1)-1:
 #       count_y += 1
 #       break
 #   elif 2**n -1 < y:
 #       y = (y-(2**n-1))
 #       count_y += 1
 #       if y != 1:
 #           y = y-1
 #       else:
 #           count_y += 1
 #           break
 # print('x',count_x, count_y)

 if count_x < count_y:
  print('1',count_y-count_x)
 elif count_y < count_x:
  print('2',count_x-count_y)
 else:
  print('0','0')


