try:
    test_case = int(input())
    for i in range(test_case):
        user = int(input())
        array = sorted(list(map(int, input().split())), reverse=True)[:user]
        c = array[len(array) - 1]
        array.remove(array[0])
        b = len(array) * c
        print(b)
except:
    pass
