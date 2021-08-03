T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    word = input()
    b_count = 0
    a_count = 0
    left_count = 0
    right_count = 0
    b_count = word.count("b")
    curr_b = 0
    for x in range(N):
        if word[x] == "b":
            curr_b += 1
        elif word[x] == "a":
            left_count += curr_b
            right_count += (b_count - curr_b)
            # print(x, left_count, right_count)
    res = K * (K + 1)
    res = res // 2
    res = res * (left_count + right_count)
    res -= K * left_count
    print(res)
