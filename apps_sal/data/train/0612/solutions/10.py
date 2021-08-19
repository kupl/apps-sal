for i in range(int(input().strip())):
    binst = input()
    result = 'Bad'
    for i in range(len(binst) - 2):
        st = binst[i:i + 3]
        if st == '101' or st == '010':
            result = 'Good'
            break
    print(result)
