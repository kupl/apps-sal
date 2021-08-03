def fibs_fizz_buzz(n):
    a, b, result = 0, 1, []
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    for i in range(len(result)):
        if result[i] % 5 == 0 and result[i] % 3 == 0:
            result[i] = "FizzBuzz"
        elif result[i] % 5 == 0:
            result[i] = "Buzz"
        elif result[i] % 3 == 0:
            result[i] = "Fizz"
    return result
