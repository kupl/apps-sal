# cook your dish here
p,s = [int(i) for i in input().split()]
scores = {}

for j in range(1, p + 1):
 sc = [int(i) for i in input().split()]
 ns = [int(i) for i in input().split()]
 nsc = dict(zip(sc,ns))
 ssc = sorted(sc)
 score = 0
 for a,b in zip(ssc[:-1], ssc[1:]):
  if nsc[a] > nsc[b]:
   score += 1
 if score in scores.keys() :
  scores[score].append(j)
 else :
  scores[score] = [j]

total_scores = sorted(list(scores.keys()))
final_list = []
for val in total_scores :
 final_list += sorted(scores[val])

for val in final_list :
 print(val)
