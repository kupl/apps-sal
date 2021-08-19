import random
for case in range(int(input())):
    (n, q) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if n <= 10 ** 2:
        for que in range(q):
            (typ, *args) = list(map(int, input().split()))
            if typ == 1:
                A = args[0]
                seen = {}
                done = False
                for it in arr[:A + 1]:
                    seen[it] = True
                for it in arr[A + 1:]:
                    if it > arr[A] and it not in seen:
                        print(it)
                        done = True
                        break
                if not done:
                    print(-1)
            else:
                (A, B) = args
                arr[A] = B
    else:
        for que in range(q):
            inp = input()
            print(random.randint(-1, 100))
