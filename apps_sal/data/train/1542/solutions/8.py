# cook your dish here
# cook your code here
t = int(input())
for i in range(t):
    num = int(input())
    arr = input()
    sc = list(map(int, input().split()))
    maxs = 0
    for z in range(num - 7):
        score = 0
        mul = 1
        for b in range(8):
            if (arr[z + b] == 'd'):
                score += sc[b] * 2
            elif (arr[z + b] == 't'):
                score += sc[b] * 3
            elif (arr[z + b] == 'D'):
                mul *= 2
                score += sc[b]
            elif (arr[z + b] == 'T'):
                mul *= 3
                score += sc[b]
            else:
                score += sc[b]
        score *= mul
        if score > maxs:
            maxs = score
    print(maxs)
