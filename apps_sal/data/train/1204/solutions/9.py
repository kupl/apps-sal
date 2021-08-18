try:
    from collections import Counter
    from sys import stdin, stdout
    def get_ints(): return map(int, stdin.readline().strip().split())
    def get_list(): return list(map(int, stdin.readline().strip().split()))
    def get_string(): return stdin.readline().strip()
    def get_singleInt(): return int(stdin.readline())

    def main():
        testCases = get_singleInt()
        for i in range(testCases):
            stringA = get_string()
            stringB = get_string()
            minOperationsRequired(stringA, stringB)

    def minOperationsRequired(stringA, stringB):
        minL = 0
        maxK = 0
        gapsList = []
        length = len(stringA)
        for i in range(length):
            if stringA[i] != stringB[i]:
                minL = minL + 1
        flag = 0
        for i in range(length):
            if stringA[i] != stringB[i]:
                if flag == 0:
                    maxK = maxK + 1
                flag = 1
            else:
                flag = 0
        fl = 1
        glE = 0
        for i in range(length):
            if stringA[i] == stringB[i]:
                if fl == 0:
                    glE = glE + 1
            else:
                if glE > 0:
                    gapsList.append(glE)
                fl = 0
                glE = 0
        gapsList = sorted(gapsList)
        minCost = minL * maxK
        for i in range(len(gapsList)):
            minL = minL + gapsList[i]
            maxK = maxK - 1
            minCost = min(minCost, minL * maxK)
        stdout.write(str(minCost) + "\n")

    def __starting_point():
        main()

except Exception:
    pass
__starting_point()
