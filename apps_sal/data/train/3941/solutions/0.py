def reverse_fizzbuzz(s):
    if s == 'Fizz': return [3]
    if s == 'Buzz': return [5]
    if s == 'Fizz Buzz': return [9, 10]
    if s == 'Buzz Fizz': return [5, 6]
    if s == 'FizzBuzz': return [15]
    s = s.split()
    for i in range(len(s)):
        if s[i].isdigit():
            start = int(s[i]) - i
            return list(range(start, start + len(s)))
