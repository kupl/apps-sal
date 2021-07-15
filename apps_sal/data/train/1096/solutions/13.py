nk = [int(i) for i in input().split()]
n = nk[0]
x = nk[1]
y = nk[2]
contests = []
time = []
while n > 0 :
 contests.append([int(i) for i in input().split()])
 n = n - 1
n = nk[0]
vworm = [int(i) for i in input().split()]
wworm = [int(i) for i in input().split()]
vworm.sort(reverse=True)
wworm.sort()
t1=0
t2=0
mint = 10**6

for contest in contests :
  if contest[1] - contest[0] > mint :
   continue

  t1 =0
  for vbus in vworm :
   if vbus <= contest[0] :
    t1 = vbus
    break

  t2=0
  for wbus in wworm :
   if wbus >= contest[1]:
    t2 = wbus
    break

  if t1 > 0 and t2 > 0 and t2 >= t1:
   t = t2 - t1 + 1
   if t <= mint  :
    mint = t


print(mint)

