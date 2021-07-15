#
# data = {1:1,0:0}
#
# for i in range(2,10**7+1):
#
#     data[i] = i**2 + data[i-1]


for t in range(int(input())):

 N = int(input())

 print((N*(N+1)*(2*N + 1))//6)


