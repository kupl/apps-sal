def max_sumDig(nMax, maxSum):
    answers = []

    for i in range(1000, nMax + 1):
        good = True
        n = [int(x) for x in str(i)]
        for j in range(0, len(n) - 3):
            if sum([n[j], n[j + 1], n[j + 2], n[j + 3]]) > maxSum:
                good = False
        if good == True:
            answers.append(i)

    num, tot = len(answers), sum(answers)
    return [num, min(answers, key=lambda x: abs(x - (tot / float(num)))), tot]
