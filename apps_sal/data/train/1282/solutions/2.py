MOD = 1000000007
a = int(input())
for i in range(a):

    x, y = list(map(int, input().split()))
    start = x
    end = y
    ans = x
    prev = x
    z = x
    j = -1
    while(start != 0):
        j += 1

        if((z & 1) != 0):

            add = 1 << j
            next = (start + add)
            if(next > end):
                ans = (ans + (((end - prev)) * (start)))

                break

            ans = (ans + ((((next - prev - 1)) * (start)) + (start - add)))

            ans %= MOD
            start -= add
            if(next == end):
                break

            prev = next

        z = z >> 1

    print(ans % MOD)
