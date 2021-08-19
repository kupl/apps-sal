# cook your dish here
noofcases = int(input())
for _ in range(noofcases):
    numqui = input().split()
    data = list(map(int, input().split()))
    for _ in range(int(numqui[1])):
        sum = 0
        startstop = list(map(int, input().split()))
        for j in range(startstop[0] - 1, startstop[1]):
            sum += data[j]
        print(sum)
