t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    prefix_xor = [arr[0]]
    for i in range(1, len(arr)):
        prefix_xor.append(prefix_xor[-1] ^ arr[i])

    xor_map = {0: [1, 0]}
    total_triplets = 0

    for index, elem in enumerate(prefix_xor):
        if elem not in xor_map:
            xor_map[elem] = [1, index + 1]
        else:
            cnt, sum_all_pos = xor_map[elem][0], xor_map[elem][1]
            total_triplets += cnt * (index + 1) - cnt - sum_all_pos
            xor_map[elem][0] += 1
            xor_map[elem][1] += (index + 1)

    print(total_triplets)
