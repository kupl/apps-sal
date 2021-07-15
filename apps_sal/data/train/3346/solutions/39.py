def prime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True
def gap(g, m, n):
    answer=[]
    i=0
    while i+m<n:
        if prime(i+m) and prime(i+m+g) and i+m+g<n:
            answer.extend([i + m, i + g + m])
            flag=True
            for j in range(1,g):
                if prime(j+i+m):
                    flag=False
                    i+=j
                    answer=[]
                    break
                else:
                    flag=True
            if flag:
                return answer
        i+=1


