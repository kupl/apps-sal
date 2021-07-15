# cook your dish here
fl = [ 0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7,
  0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
  0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3,
  0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

def log2(num) :
 i = -1
 while num>0 :
  i+=1
  num//=2
 return i

cycle = 60
for _ in range(int(input())) :
 n = int(input())
 target = (2**(log2(n)))%60
 print(fl[target-1])
