l1 = input().lower()
lang_set = set([x.lower() for x in l1 if x.isalpha() ])
l2 = set([x for x in l1 if l1.count(x)>1])

no_cases = int(input())
# if(len(l2)>0):
#     for i in xrange(no_cases):
#         word = raw_input()
#         print "No"
# else :
for i in range(no_cases):
 word = input().lower()
 word_set = set([x.lower() for x in word if x.isalpha() ])
 fl =word_set.issubset(lang_set)
 if(fl) :
  print("Yes")
 else :
  print("No")
