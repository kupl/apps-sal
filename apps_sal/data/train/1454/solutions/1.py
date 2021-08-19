N = 10 ** 3 + 1
t = eval(input())
inp = ()
bag = [[0 for j in range(ord('z'))] for i in range(N + 1)]
while t:
    t -= 1
    inp = input().split()
    if inp[0] == '1':
        bag[int(inp[1])][ord(inp[3]) - ord('a')] += int(inp[2])
    if inp[0] == '2':
        sum = 0
        for i in range(int(inp[1]), int(inp[2]) + 1):
            sum += bag[i][ord(inp[3]) - ord('a')]
        print(sum)
