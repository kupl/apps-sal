while True:
    try:
        n = input()
        arr = []
        n = int(n)
        start = int(n - 100)
        if start <= 0:
            start = int(1)

        counter = int(0)
        for i in range(start, n):
            tp = int(i)
            ans = int(0)
            while tp != 0:
                ans += int(tp % 10)
                tp /= 10

            ans += int(i)

            if ans == n:
                counter += 1
                arr.append(int(i))

        if counter == 0:
            print(0)
        else:
            print(counter)
            for i in range(0, counter):
                print(arr[i])

    except:
        break
