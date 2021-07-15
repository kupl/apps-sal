def solve_equal(lst,no_of_elem_in_group):
 dist = 0
 for i in lst:
  if i > no_of_elem_in_group:
   dist += abs(no_of_elem_in_group-i)
 return dist

def solve(lst,l,no_of_group):
 no_of_elem_in_group = l//no_of_group
 list_len = len(lst)
 dist = 0
 if no_of_group >= list_len:
  return solve_equal(lst,no_of_elem_in_group)

 else:  # no_of_group < list_len
  lst.sort()
  dist = sum(lst[0:list_len-no_of_group])
  return dist + solve_equal(lst,no_of_elem_in_group)

T = int(input())
for z in range(T):
 dct = {}
 s = list(input())
 for elem in s:
  try:
   dct[elem] += 1
  except:
   dct[elem] = 1
   
 lst = list(dct.values())
 l = len(s)
 mn = 99999999999999999
 for i in range(1,min(l+1,27)):
  no_of_group = i
  if l%no_of_group == 0:
   lst2 = lst[:]
   tmp = solve(lst2,l,no_of_group)
   #print(i,tmp)
   if tmp < mn:
    mn = tmp
 print(mn)

