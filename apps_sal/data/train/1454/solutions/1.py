N = 10**3 + 1
t = eval(input())
inp = ()
bag = [[0 for j in range(ord('z'))] for i in range(N + 1)]
# print bag
while t:
    t -= 1
    inp = input().split()
    if inp[0] == "1":
        # print "enter"
        bag[int(inp[1])][ord(inp[3]) - ord('a')] += int(inp[2])

    if inp[0] == "2":
        sum = 0
        for i in range(int(inp[1]), int(inp[2]) + 1):
            sum += bag[i][ord(inp[3]) - ord('a')]
        print(sum)

#
# for j in range(ord('z')-ord('a')):
#     for i in range(N+1):
#         if bag[i][j]!=0:
#             print bag[i][j] ,i,j
