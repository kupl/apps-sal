for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    count = []
    jars = [arr[0]]
    prev = arr[0]
    curr_count = 1
    flag = True
    for a in arr[1:]:
        if a != prev:
            if a in jars or curr_count in count:
                flag = False
                break
            jars.append(a)
            count.append(curr_count)
            curr_count = 1

        else:
            curr_count += 1
        prev = a

    if curr_count in count:
        flag = False

    print("YES" if flag else "NO")
