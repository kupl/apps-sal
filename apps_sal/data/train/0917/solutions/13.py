for _ in range(int(input())):
    (n, k) = map(int, input().split())
    list1 = list(map(int, input().split()))
    list1.sort()
    min1 = 1000000000000001
    maxsum = 0
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            temp = abs(list1[i] + list1[j] - k)
            if temp < min1:
                min1 = min(min1, temp)
    if min1 != 0:
        cand1 = k + min1
        cand2 = k - min1
        s = list()
        cnt = 0
        for i in list1:
            t1 = cand1 - i
            if t1 in s:
                cnt += s.count(t1)
            t2 = cand2 - i
            if t2 in s:
                cnt += s.count(t2)
            s.append(i)
        print(min1, cnt)
    else:
        cand = k + min1
        s = list()
        cnt = 0
        for i in list1:
            t1 = cand - i
            if t1 in s:
                cnt += s.count(t1)
            s.append(i)
        print(min1, cnt)
