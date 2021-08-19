for _ in range(int(input())):
    (N, K) = (int(i) for i in input().strip().split())
    stair_arr = [0]
    stair_arr.extend([int(i) for i in input().strip().split()])
    add_cnt = 0
    for i in range(1, N + 1):
        height_diff = stair_arr[i] - stair_arr[i - 1]
        if height_diff > K:
            add_cnt += height_diff // K
            if height_diff % K == 0:
                add_cnt -= 1
    print(add_cnt)
