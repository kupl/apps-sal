def find_unknown_number(x,y,z):
    answer = 1
    i = 1
    n = 106
    
    while i < n:
        if i % 3 == x and i % 5 == y and i % 7 == z:
            answer = i
            break
        i = i + 1
    return answer
