def zeros(n):
    answer = 0
    for i in range(1,100):
        answer += (int(n/5**i))
    
    return answer

