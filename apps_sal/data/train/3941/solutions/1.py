def reverse_fizzbuzz(string):
    s = string.split()
    lst = [0] * len(s)
    for indx, i in enumerate(s):
        if i.isdigit():
            lst[indx] = int(i)
            return list(range(lst[indx] - indx, lst[indx] + len(s) - indx))
    return {'Fizz': [3], 'Buzz': [5], 'FizzBuzz': [15], 'Buzz Fizz': [5, 6], 'Fizz Buzz': [9, 10]}[string]
