# cook your dish here
t = int(input())
for i in range(t):
    current = 0
    count = 0
    n, k = [int(x) for x in input().split()]
    h = [int(y) for y in input().split()]
    for j in range(100000000):
        # print(current)
        if current == h[-1]:
            break

        for aa in range(100000000):

            if abs(current - h[j]) <= k:
                current = h[j]
                break
            else:
                # for
                current += k
                # print(current)
                count += 1
    print(count)

    # for j in range(10000000):
    #     print(current)
    #     if current+abs(hi[j]-hi[j+1])<=k:
    #         current=hi[j]
    #         if current==hi[-1]:
    #             break

    #     else:
    #         current+=k
    #         count+=1
    # # print(count)
