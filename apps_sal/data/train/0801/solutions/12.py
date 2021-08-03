t = int(input())
while t > 0:
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    resultant, s = [], set()
    for i in range(0, len(arr1)):
        s.add(arr1[i])
        resultant.append(arr1[i])
    for i in range(0, len(arr2)):
        s.add(arr2[i])
        resultant.append(arr2[i])
    checker = 0
    for i in resultant:
        if resultant.count(i) % 2 == 1:
            checker = 1
            print(-1)
            break
    if checker == 0:
        vector = []
        for i in s:
            temp = resultant.count(i) / 2
            if temp < arr1.count(i):
                while arr1.count(i) - temp:
                    vector.append(i)
                    temp += 1
            elif temp < arr2.count(i):
                while arr2.count(i) - temp:
                    vector.append(i)
                    temp += 1
        vector.sort()
        mini = 2 * min(min(arr1), min(arr2))
        ans = 0
        for i in range(0, len(vector) // 2):
            ans += min(mini, vector[i])
        print(ans)

    t -= 1
