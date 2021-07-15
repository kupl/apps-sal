def evil(n):
    return ["It\'s Odious!", "It\'s Evil!"][str(bin(n)).count('1')%2==0]
