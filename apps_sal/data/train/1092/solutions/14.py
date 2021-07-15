# cook your dish here
for test in range(0,int(input())):
 N,K,E,M = map(int,input().split())
 scores = []
 for i in range(0,N-1):
  scores.append(sum(list(map(int,input().split()))))
 sergey_score = sum(list(map(int,input().split())))
 scores.sort()
 #using max because maybe Sergey's two exam scores are sufficient to qualify
 req_score = max(scores[N-K-1]-sergey_score+1,0)
 
 if req_score<=M:
  print(req_score) 
 else:
  print("Impossible")
