N = 100100


def main():
    n = int(input())
    d = [0] * N
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    m, c = [0] * N, [0] * N
    m[0] = b[0]
    c[0] = d[0]

    z = 1
    p = 0
    for i in range(1, n):
        p = min(p, z)
        while(p + 1 < z and m[p + 1] * a[i] + c[p + 1] <= m[p] * a[i] + c[p]):
            p = p + 1
        d[i] = m[p] * a[i] + c[p]
        while(z >= 2 and (c[z - 2] - c[z - 1]) * (b[i] - m[z - 1]) >= (c[z - 1] - d[i]) * (m[z - 1] - m[z - 2])):
            z = z - 1
        m[z], c[z] = b[i], d[i]
        z = z + 1
    #for j in range(n):print(d[j])
    print(d[n - 1])


main()


# Made By Mostafa_Khaled
