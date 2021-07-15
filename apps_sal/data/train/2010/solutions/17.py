def main():
    n = int(input())
    hts = list(map(int,input().split()))
    dpleft = [1]
    for i in range(1,n):
        dpleft.append(min(hts[i],dpleft[-1]+1))

    hts.reverse()
    dpright = [1]
    for i in range(1,n):
        dpright.append(min(hts[i],dpright[-1]+1))

    dpright.reverse()
    ans = 0
    for i in range(n):
        ans = max(ans,min(dpleft[i],dpright[i]))

    print(ans)

main()

