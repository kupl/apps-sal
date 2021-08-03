def reverse_fizzbuzz(s):
    s = s.split()
    d = next((i for i, j in enumerate(s) if j.isdigit()), -1)
    if d != -1:
        return list(range(int(s[d]) - len(s[:d]), int(s[d]) + len(s[d:])))
    else:
        if s in [['Fizz'], ['Buzz']]:
            return [[3], [5]][s == ['Buzz']]
        if s == ['FizzBuzz']:
            return [15]
        if s == ['Fizz', 'Buzz']:
            return [9, 10]
        return [5, 6]
