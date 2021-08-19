def suma(s, e, cnt):
    t = e - s
    if cnt < e:
        t_1 = e - cnt + 1
        ans = t * (t + 1) // 2 - t_1 * (t_1 + 1) // 2
    else:
        ans = t * (t + 1) // 2 - 1
    return ans


(n, m, w, b, *l) = list(map(int, input().split()))
dic = {}
for i in range(0, 2 * w, 2):
    (y, x) = (l[i] - 1, l[i + 1] - 1)
    if y not in dic:
        dic[y] = [[x, 1]]
    else:
        dic[y].append([x, 1])
for i in range(2 * w, 2 * (w + b), 2):
    (y, x) = (l[i] - 1, l[i + 1] - 1)
    if y not in dic:
        dic[y] = [[x, 2]]
    else:
        dic[y].append([x, 2])
ans = 0
for v in list(dic.values()):
    v.sort()
    v.append([m - 1, 2])
    i = len(v) - 1
    cnt_i = m + 1
    ans += 1
    while i >= 0:
        if i - 1 >= 0 and v[i - 1][1] == 2:
            ans += suma(v[i - 1][0], v[i][0], cnt_i)
            cnt_i = v[i - 1][0]
            i -= 1
        elif i - 2 >= 0 and v[i - 2][1] == 1:
            ans += suma(v[i - 2][0], v[i][0], cnt_i)
            if cnt_i != v[i - 1][0]:
                ans -= v[i][0] - v[i - 1][0] + 1
            cnt_i = v[i - 2][0]
            i -= 1
        elif i - 2 >= 0 and v[i - 2][1] == 2:
            ans += suma(v[i - 2][0], v[i][0], cnt_i)
            if cnt_i != v[i - 1][0]:
                ans -= v[i][0] - v[i - 1][0] + 1
            cnt_i = v[i - 2][0]
            i -= 2
        else:
            ans += suma(-1, v[i][0], cnt_i)
            if i == 1 and cnt_i != v[i - 1][0]:
                ans -= v[i][0] - v[i - 1][0] + 1
            break
n -= len(dic)
ans += n * m * (m + 1) // 2
print(ans)
