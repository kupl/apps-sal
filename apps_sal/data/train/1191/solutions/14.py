from collections import Counter
test = int(input())
for _ in range(test):
    n, q = list(map(int, input().split(' ')))
    correct = []
    wrong = []
    for j in range(n):
        mydict = input()
        if mydict not in correct:
            correct.append(mydict)

    for i in range(q):
        misspelt = input()
        wrong.append(misspelt)
    for k in range(len(wrong)):
        for j in range(len(correct)):
            value = Counter(wrong[k]) - Counter(correct[j])
            if len(value) == 1:
                print(correct[j])
            if len(value) == 0:
                print(correct[j])
