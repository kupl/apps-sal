# cook your dish here
T = int(input())

max_score = []

for _ in range(T):

 N = int(input())
 string = input()
 score = input().split()
 score = list(map(int, score))

 
 noi = (N - 8 + 1)

 maximum = 0 
 
 for i in range(noi):

  dd = 0
  ttt = 0
  scrs = string[i:i+8]

  num_scrs = []
  for scr in scrs:

   if scr == '.':
    num_scrs.append(1)

   elif scr == 'd':
    num_scrs.append(2)

   elif scr == 't':
    num_scrs.append(3)

   elif scr == 'D':
    num_scrs.append(1)
    dd += 1

   elif scr == 'T':
    num_scrs.append(1)
    ttt += 1

  s = 0
  
  for i in range(8):
   s += num_scrs[i]*score[i]

  s *= 2**dd
  s *= 3**ttt

  if s > maximum:
   maximum = s
  
 max_score.append(maximum)


for s in max_score:

 print(s)

