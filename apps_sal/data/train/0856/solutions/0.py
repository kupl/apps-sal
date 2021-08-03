t = int(input())

for _ in range(t):
    n = int(input())

    a = {}

    for i in range(n):
        l = input()

        if l not in a:
            a[l] = 1
        else:
            a[l] += 1

    done = []
    ans = 0

    for i in a:
        if a[i] != 0:
            temp = [x for x in i.split()]
            v = temp[0]

            v0 = v + " 0"
            v1 = v + " 1"

            if(v0 in a and v1 in a):
                if a[v0] > a[v1]:
                    ans += a[v0]
                else:
                    ans += a[v1]

                a[v0] = a[v1] = 0
            elif(v0 in a):
                ans += a[v0]
                a[v0] = 0
            elif(v1 in a):
                ans += a[v1]
                a[v1] = 0

    print(ans)
