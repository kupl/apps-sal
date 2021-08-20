n = int(input())
a = [*[int(x) - 1 for x in input().split()]]
'count = [1] * n\nreal_position = [[] for i in range(n)]\nposition = [0] * (2 * n)\nfor i in range(2*n):\n\tposition[i] = count[a[i]]\n\tcount[a[i]] = -1\n\treal_position[a[i]].append(i)\n\n#print(position)\nsum = [i for i in position]\nfor i in range(1, 2*n):\n\tsum[i] += sum[i - 1]\n\t\n\nans1 = 0\nfor i in range(n):\n\tans1 += (sum[real_position[i][1] - 1] - sum[real_position[i][0]])\n\n#ans = -(ans // 2)\n#print(ans)\nans = 0\nfor i in range(n):\n\tans += (real_position[i][1] - real_position[i][0] - 1)\n\nprint(ans - ans1)\n'
ans = 0
f = [True] * n
for i in range(2 * n - 1):
    if f[a[i]]:
        j = i + 1
        while a[j] != a[i]:
            if f[a[j]]:
                ans += 1
            j += 1
        f[a[i]] = False
print(ans)
