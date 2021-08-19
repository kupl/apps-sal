for _ in range(int(input())):
    noOfGirls = int(input())
    boys = list(input().split())
    freq = dict()
    for j in boys:
        if j not in freq:
            freq[j] = 1
        else:
            freq[j] += 1
    occu = list(freq.values())
    occu.sort()
    answers = list()
    for (key, value) in freq.items():
        if value == occu[-1]:
            answers.append(key)
    if len(answers) != 1:
        answers.sort()
        print(*answers[0], sep='')
    else:
        print(*answers, sep='')
