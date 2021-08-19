def main():
    n, k, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    dp = [-1]
    for i in range(n):
        if arr[i] > 0:
            dp.append(i)
        else:
            dp.append(dp[-1])

    dp.pop(0)
    start = 0
    count = 0
    total = 0
    ans = 0
    index = -1
    rem = k
    # print(dp)
    for i in range(n):
        if index != -1:
            if i - index <= rem:
                # print('here',i,index)
                arr[i] *= m
            else:
                index = -1

        total += arr[i]
        count += 1
        if count == k:
            # print(total,start,i)
            count -= 1
            if total < m:
                index = dp[i]
                if index == -1 or i - index + 1 > k:
                    print(-1)
                    return

                # print(index)
                rem = k - (i - index + 1)
                # print('what',rem)
                total -= arr[index]
                arr[index] *= m
                total += arr[index]
                ans += 1
                index = i

            total -= arr[start]
            start += 1

    # print(arr)
    print(ans)


main()
