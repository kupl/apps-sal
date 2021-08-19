
def reverse_fizzbuzz(string):
    dic = {'Fizz': 3, 'Buzz': 5, 'FizzBuzz': 15, 'Buzz Fizz': 5, 'Fizz Buzz': 9}  # if only strings, those are the starting positions
    split = string.split()

    # if contains number, find fist and return which number is first in original fizzbuzz string
    # if there is no number, must be one of the situation in dic, which will give starting number for each of those
    start = next((int(y) - x for x, y in enumerate(split) if y.isdigit()), dic.get(string))
    return list(range(start, start + len(split)))
