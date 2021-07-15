#Vision and the MindStone
N,K = map(int,input().split())
data = list(map(int,input().split()))
output = []
output.append(data)
add = [data[0]]
for i in range(N-1):
    add.append(0)
for i in range(K):
    output.append(add)
for i in range(1,K+1):
    for j in range(1,N):
        output[i][j] = output[i-1][j] + output[i][j-1]
for i in output[K]:
    print(i%(10**9 + 7),end=" ")
