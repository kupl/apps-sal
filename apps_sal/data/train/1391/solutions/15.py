# cook your dish here
def fn_bonAppetit(test):
 for _ in range(test):
  n, k = map(int, input().split())
  cust_preference = {}
  for c in range(n):
   s, f, p = map(int, input().split())
   if p not in cust_preference:
    cust_preference[p] = [(s, f)]
   else:
    cust_preference[p].append((s, f))
  count = 0
  for v in cust_preference.values():
   v.sort(key = lambda x: x[1])
   previous = (0, 0)
   for item in v:
    if item[0] >= previous[1]:
     previous = item
     count += 1
  print(count)
  
test=int(input())
fn_bonAppetit(test)
