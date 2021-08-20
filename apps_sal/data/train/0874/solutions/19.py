import math
no_of_test_cases = int(input())


def maxTopics(hours, N, M, S):
    sorted_hours = sorted(hours)
    no_of_days_needed = []
    for x in sorted_hours:
        if math.ceil(x / S) <= 2:
            no_of_days_needed.append(math.ceil(x / S))
    no_of_topics_coverd = 0
    for x in no_of_days_needed:
        if M - x >= 0:
            no_of_topics_coverd += 1
            M = M - x
    return no_of_topics_coverd


for x in range(1, no_of_test_cases + 1):
    (N, M, S) = input().split(' ')
    N = int(N)
    M = int(M)
    S = int(S)
    hours = list([int(x) for x in input().split(' ')])
    print(maxTopics(hours, N, M, S))
