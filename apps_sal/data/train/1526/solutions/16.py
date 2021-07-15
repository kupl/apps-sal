import time
import math
import random
import string

def log2(x):
 return math.log(x, 2)

MAX = log2(1e7)
MIN = log2(1e-7)

start_time = time.time()

vowels = 'aeiou'
v = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
abets = string.ascii_lowercase

tcs = int(input())

for test in range(tcs):
 l = int(input())
 a = []
 b = []
 for _ in range(l):
  flag = False
  s = input()
  for i in range(len(s)-2):
   if s[i] not in vowels:
    if s[i+1] not in vowels or s[i+2] not in vowels:
     flag = True
     break
   else:
    if s[i+1] not in vowels and s[i+2] not in vowels:
     flag = True 
     break
  if flag:
   b.append(s)
  else:
   a.append(s)
 # for wer in range(l):
 #     s = input()
 #     n = len(s)
 #     c1 = 0
 #     for i in range(n):
 #         if s[i] not in v:
 #             if i+1 < n:
 #                 if s[i+1] not in v:
 #                     c1 = 1
 #                     break
 #             if i+2 < n:
 #                 if s[i+2] not in v:
 #                     c1 = 1
 #                     break
 #     if c1 == 1:
 #         b.append(s)
 #     else:
 #         a.append(s)
 alen = len(a)
 blen = len(b)
 # ################ Alice ##############
 achar_dict = {}
 atotal_dict = {}
 for recipe in a:
  d = {}
  for ch in recipe:
   d[ch] = 1
   if atotal_dict.get(ch):
    atotal_dict[ch] += 1
   else:
    atotal_dict[ch] = 1
  for ch in d:
   if achar_dict.get(ch):
    achar_dict[ch] += 1
   else:
    achar_dict[ch] = 1
 ################ Bob ##############
 bchar_dict = {}
 btotal_dict = {}
 for recipe in b:
  d = {}
  for ch in recipe:
   d[ch] = 1
   if btotal_dict.get(ch):
    btotal_dict[ch] += 1
   else:
    btotal_dict[ch] = 1
  for ch in d:
   if bchar_dict.get(ch):
    bchar_dict[ch] += 1
   else:
    bchar_dict[ch] = 1
 ################## Calculation ##################
 result = 0
 for i in achar_dict:
  result += log2(achar_dict[i]) - alen*log2(atotal_dict[i])
  
 for i in bchar_dict:
  result += blen*log2(btotal_dict[i]) - log2(bchar_dict[i])

 if result > MAX:
  print('Infinity')
 elif result < MIN:
  print(0)
 else:
  print(2**result)
  # print('%.7f' % 10**result)

# print(time.time() - start_time)

