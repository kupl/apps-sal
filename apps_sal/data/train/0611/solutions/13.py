try:
    t = int(input())
    for i in range(t):
        n = int(input())
        z = 0
        a = [int(j) for j in input().split(" ")]
        # print(a)
        for k in range(n - 1):
            # print("a")
            for x in range(k + 1, n):
                # print(a[k],a[x])
                if a[k] != a[x]:
                    if a[a[k] - 1] == a[a[x] - 1]:
                        print("Truly Happy")
                        # print("c")
                        z = 1
                        break
            if z == 1:
                break

        if z == 0:
            # print("e")
            print("Poor Chef")
        # print("................................."
except:
    pass
