#data = open("P5.txt")
n, k = list(map(int, input().split()))
tweets = [False] * n
count = 0
for _ in range(k):
    stuff = input().split()
    if stuff[0] == "CLICK":
        i = int(stuff[1]) - 1
        if tweets[i]:
            count -= 1
        else:
            count += 1
        tweets[i] = not tweets[i]
    else:
        tweets = [False] * n
        count = 0
    print(count)
