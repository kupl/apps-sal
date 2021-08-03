def bits_war(numbers):
    FIGHT = sum(sum(map(int, bin(abs(n))[2:])) * (-1)**(n < 0) * (-1)**(n % 2 == 0) for n in numbers)
    return ["evens win", "tie", "odds win"][(FIGHT >= 0) + (FIGHT > 0)]
