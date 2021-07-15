for t in range(int(input())):
 e_islands = []
 u_islands = []
 s = input()
 r = input()
 gap = 0
 size = 0
 mismatches = 0
 for i in range(len(s)):
  if s[i] == r[i]:
   gap += 1
   if size != 0:
    u_islands.append(size)
    size = 0
  else:
   size += 1
   if gap != 0:
    e_islands.append(gap)
    gap = 0
   mismatches += 1
 if size != 0:
  u_islands.append(size)
 if s[0] == r[0]:
  e_islands = e_islands[1:]
 e_islands = sorted(e_islands)
 # print(mismatches)
 # print(e_islands)
 # print(u_islands)
 min_len = mismatches
 k = len(u_islands)
 ans = min_len * k
 for val in e_islands:
  min_len += val
  k -= 1
  ans = min(ans, min_len * k)
 print(ans)

