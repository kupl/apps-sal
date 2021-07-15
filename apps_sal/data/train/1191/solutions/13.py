"""
from collections import Counter
test = int(input())
for _ in range(test):
    n, q = map(int, input().split(' '))
    correct = []
    # corrected = set(corrected)
    wrong = []
    for j in range(n):
     mydict = input()
     if mydict not in correct:
      correct.append(mydict)

    for i in range(q):
     misspelt = input()
     wrong.append(misspelt)
    for k in range(len(wrong)):
     for j in range(len(correct)):
      value = Counter(wrong[k]) - Counter(correct[j])
      if len(value) == 1:
       print(correct[j])
      if len(value) == 0:
       print(correct[j])
"""

from collections import Counter

test = int(input())
for _ in range(test):
 n, q = list(map(int, input().split(' ')))
 correct = []
 allcorrect = []
 allwrong = []
 # corrected = set(corrected)
 wrong = []
 for j in range(n):
  mydict = input()
  if mydict not in correct:
   correct.append(mydict)
 for f in range(len(correct)):
  allcorrect.append(Counter(correct[f]))

 for i in range(q):
  misspelt = input()
  wrong.append(misspelt)
 for s in range(len(wrong)):
  allwrong.append(Counter(wrong[s]))
 for k in range(len(wrong)):
  for j in range(len(correct)):
   value = allwrong[k] - allcorrect[j]
   if len(value) == 1:
    print(correct[j])
   if len(value) == 0:
    print(correct[j])

