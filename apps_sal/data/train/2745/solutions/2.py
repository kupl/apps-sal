def tower_of_hanoi(rings):
    answer = 1
    for i in range(rings-1):
        answer = (answer *2) +1
    return answer
