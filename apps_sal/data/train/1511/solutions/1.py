# cook your dish here

def solve(Str, K):
 S = ''
 ind = -1
 iron, mag = [], []
 for it in Str:
  ind += 1
  if it == ':':
   ind += 1

  if it == 'I':
   iron.append(ind)
  elif it == 'M':
   mag.append(ind)

 ans = 0
 lr = len(iron)
 lm = len(mag)

 i, j = 0, 0
 while i<lr and j<lm:
  ir, mg = iron[i], mag[j]
  if abs(ir - mg) <= K:
   ans += 1
   i+=1
   j+=1
  else:
   if ir > mg:
    j += 1
   else:
    i += 1
 return ans

for case in range(int(input())):
 n, k = list(map(int, input().split()))
 st = input()
 li = [it for it in st.split('X') if len(it)>0]

 ans = sum(solve(string, k) for string in li)
 print(ans)

