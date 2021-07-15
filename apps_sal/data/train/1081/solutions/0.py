# cook your dish here
import string 
from collections import OrderedDict
from itertools import zip_longest
dic = OrderedDict(zip(string.ascii_uppercase, range(0, 26)))
keys = [98, 57, 31, 45, 46]
t = int(input()) # number of test cases
s1 = []
for i in range(t):
  s = input()
  for i in s:
    if i in dic.keys():
      s1.append(int(i.replace(i, str(dic[i]))))
  s2 = [sum(t) for t in zip_longest(s1, keys, fillvalue=0)]
  inv_dic = {v:k for k,v in dic.items()}
  s_1 = list()
  for i in range(len(s1)):
    s_1.append(s2[i]%26)
  res= [inv_dic[i] for i in s_1]
  print(''.join(res))
  inv_dic.clear()
  res.clear()
  s1.clear()
  s2.clear()
  s_1.clear()
