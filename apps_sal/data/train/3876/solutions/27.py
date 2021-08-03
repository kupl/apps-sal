def find(n):
    divideBy5 = n // 5
    divideBy3 = n // 3
    divideBy15 = n // 15
    sum = (5 * divideBy5 + 5) * divideBy5 // 2 + (3 * divideBy3 + 3) * divideBy3 // 2 - (15 * divideBy15 + 15) * divideBy15 // 2
    return sum
