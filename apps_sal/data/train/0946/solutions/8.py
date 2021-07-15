N,K = map(int,input().split(" "))


ball =[]
for i in range(N):
 ball.append(list(map(int,input().split(' '))))

prob =[[0 for i in range(K)] for j in range(N)]

for i in range(N):
 temp = 0
 for j in range(K):
  temp += ball[i][j]
 ball[i].append(temp)

for i in range(K):
 prob[0][i] = ball[0][i]/ball[0][K]

for i in range(1,N):
 c = ball[i][K]
 for j in range(0,K):
  b = ball[i][j]
  prob[i][j] = (b + prob[i-1][j])/(c+1)
 

# print(ball)

# print("jeiasjf")

# print(prob)

for i in range(K):
 print("%.6f" % prob[N-1][i] , end=" ")
# print(*prob[N-1])
