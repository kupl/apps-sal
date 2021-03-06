def reverse_fizzbuzz(string):
    dic = {'Fizz': 3, 'Buzz': 5, 'FizzBuzz': 15, 'Buzz Fizz': 5, 'Fizz Buzz': 9}
    split = string.split()
    start = next((int(y) - x for (x, y) in enumerate(split) if y.isdigit()), dic.get(string))
    return list(range(start, start + len(split)))
