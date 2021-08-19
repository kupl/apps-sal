try:
    for _ in range(int(input())):
        s = input()
        size = len(s)
        m = size * (size - 1) // 2
        n = size
        answer = 0
        for i in range(size - 1):
            if s[i] == s[i + 1]:
                answer += m
            else:
                answer += n
        print(answer)
except Exception as e:
    print(e)
