def segments(m, a):
    answer = [i for i in range(m+1)]
    for i in a:
        for j in range(i[0], i[1]+1):
            try:
                answer.remove(j)
            except ValueError:
                pass
    return answer
