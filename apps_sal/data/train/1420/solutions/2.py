import math


def find_interleavings_2(a, b, i, j):
 try:
  return lev_memo[(i, j)], nbs_memo[(i, j)]
 except KeyError:
  pass
 to_return = []
 nbs = []
 if i == len(a) and j == len(b):
  return [[]], [0]
 elif i == len(a):
  leaves, nbs1 = find_interleavings_2(a, b, i, j + 1)
  for ind in range(len(leaves)):
   leaf = leaves[ind]
   to_return.append([b[j]] + leaf)
   if len(leaf) == 0:
    nbs.append(nbs1[ind] + 1)
   elif leaf[0] == b[j]:
    nbs.append(nbs1[ind])
   else:
    nbs.append(nbs1[ind] + 1)
 elif j == len(b):
  leaves, nbs1 = find_interleavings_2(a, b, i + 1, j)
  for ind in range(len(leaves)):
   leaf = leaves[ind]
   to_return.append([a[i]] + leaf)
   if len(leaf) == 0:
    nbs.append(nbs1[ind] + 1)
   elif leaf[0] == a[i]:
    nbs.append(nbs1[ind])
   else:
    nbs.append(nbs1[ind] + 1)
 else:
  leaves, nbs1 = find_interleavings_2(a, b, i, j + 1)
  for ind in range(len(leaves)):
   leaf = leaves[ind]
   to_return.append([b[j]] + leaf)
   if len(leaf) == 0:
    nbs.append(nbs1[ind] + 1)
   elif leaf[0] == b[j]:
    nbs.append(nbs1[ind])
   else:
    nbs.append(nbs1[ind] + 1)

  leaves2, nbs2 = find_interleavings_2(a, b, i + 1, j)
  for ind in range(len(leaves2)):
   leaf = leaves2[ind]
   to_return.append([a[i]] + leaf)
   if len(leaf) == 0:
    nbs.append(nbs1[ind] + 1)
   elif leaf[0] == a[i]:
    nbs.append(nbs2[ind])
   else:
    nbs.append(nbs2[ind] + 1)

 lev_memo[(i, j)] = to_return
 nbs_memo[(i, j)] = nbs
 return to_return, nbs


for _ in range(int(input())):
 n, m, k = list(map(int, input().split(" ")))
 a = list(map(int, input().split(" ")))
 b = list(map(int, input().split(" ")))
 res = 0

 lev_memo = dict()
 nbs_memo = dict()
 ils, numBlo = find_interleavings_2(a, b, 0, 0)
 ils = [tuple(x) for x in ils]
 #print(ils, numBlo)
 memo = dict()
 for c in numBlo:
  if c == k:
   res += 1

 print(res)

