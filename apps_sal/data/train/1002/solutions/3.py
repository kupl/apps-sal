for _ in range(int(input())):
    n, d = map(int, input().split())
    li = list(map(int, input().split()))
    ini = li[0]
    li.sort()
    tvl = 1
    nidx = li.index(ini)
    for i in range(n - 1):
        if li[i + 1] - li[i] > d:
            tvl = 0
            break
    flag = 0
    if tvl:
        if(nidx != 0 or nidx != n - 1):
            i = nidx
            while(i < n - 1):
                if li[i + 1] - li[i - 1] > d:
                    tvl = 0
                    break
                else:
                    if(i == n - 2):

                        break
                    else:
                        if(li[i + 2] - li[i] <= d):
                            i += 2
                        else:
                            tvl = 0
                            break
            if not tvl:
                i = nidx
                while(i > 0):
                    if li[i + 1] - li[i - 1] > d:
                        tvl = 0
                        break
                    else:
                        if(i == 1):
                            flag = 1
                            break
                        else:
                            if(li[i] - li[i - 2] <= d):
                                i -= 2
                            else:
                                tvl = 0
                                break
                if((i == 1 and flag) or i == 0):
                    tvl = 1
    if(tvl == 0):
        print("NO")
    else:
        print("YES")
