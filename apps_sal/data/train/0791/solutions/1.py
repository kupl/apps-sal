for _ in range(eval(input())):
    n, d = list(map(int, input().strip().split()))
    l = list(map(int, input().strip().split()))
    main_flag = 0
    final_count = 0
    total = sum(l)
    if total % n != 0:
        print(-1)
        continue
    else:
        expected_value = total / n
        for i in range(d):
            delta = []
            j = i
            while j < n:
                delta.append(expected_value - l[j])
                j += d
            diff = 0
            curr_diff = 0
            flag = 0
            count = 0
            for k in range(len(delta)):
                if diff != 0 and flag:
                    count += abs(diff)
                if delta[k] != 0:
                    diff += delta[k]
                    if diff == 0:
                        flag = 0
                    else:
                        flag = 1
            if flag == 0:
                final_count += count
            else:
                main_flag = 1
                break
    print(final_count if not main_flag else -1)
