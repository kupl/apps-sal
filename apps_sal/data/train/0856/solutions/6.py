# by nikkipinky
for _ in range(int(input())):
    n = int(input())
    countPairs = dict()
    for i in range(n):
        word, spam = input().split()
        spam = int(spam)
        if(word not in countPairs):
            countPairs[word] = [0, 0]
        countPairs[word][spam] += 1
    finalcount = 0
    for i in countPairs:
        finalcount += max(countPairs[i])
    print(finalcount)
