t = int(input())
while t > 0:
    N = int(input())
    dress_price = list(map(int, input().split()))
    flag = 0
    dress_price.sort(reverse=True)
    for i in range(N):
        if dress_price[i] < 2000:
            k1 = 2000 - dress_price[i]
            if k1 in dress_price[i + 1:]:
                flag = 1
                break

    if flag == 1:
        print("Accepted")
    else:
        print("Rejected")

    t = t - 1
