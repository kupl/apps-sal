test_case = int(input())
while test_case:

    passage = input()
    n = len(passage)

    count_days = 0
    jump = 0
    i = 0
    while i < n:

        if passage[i] == '.':
            count_empty = 1
            k = i + 1
            while(passage[k] == '.'):
                count_empty += 1
                k += 1
            if count_empty > jump:
                count_days += 1
                jump = count_empty

            i = k
        else:
            i += 1

    print(count_days)
    test_case -= 1
