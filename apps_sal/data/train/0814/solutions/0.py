for _ in range(int(input())):
    n = int(input())

    def maxConsequtiveOnes(lst):
        _max = 0
        _ones = [0]
        for i in lst:
            if i == 0:
                _max += 1
            if i == 1:
                _max = 0
            _ones.append(_max)
        return max(_ones)

    a = list(map(int, input().split()))
    b = maxConsequtiveOnes(a)
    if (b % 2 == 0):
        print("No")
    else:
        print("Yes")
