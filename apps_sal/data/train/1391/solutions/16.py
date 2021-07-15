def fn_bonAppetit(t):
 for test_case in range(t):
  # num of customers (n), num of compartments (k)
  n, k = map(int, input().split())
  cust_preference = {}
  # looping through each customer
  for c in range(n):
   # start, finish and preference
   s, f, p = map(int, input().split())
   if p not in cust_preference:
    cust_preference[p] = [(s, f)]
   else:
    cust_preference[p].append((s, f))
  
  count = 0
  for v in cust_preference.values():
   v.sort(key = lambda x: x[1]) # sort by finish time in-place
   previous = (0, 0)
   for item in v:
    if item[0] >= previous[1]:
     previous = item
     count += 1
  print(count)
  
t = int(input()) # total number of test cases
fn_bonAppetit(t)
