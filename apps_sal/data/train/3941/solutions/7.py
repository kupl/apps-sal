def reverse_fizzbuzz(s):
    no_int = {"Fizz": 3, "Buzz": 5, "Buzz Fizz": 5, "Fizz Buzz": 9, "FizzBuzz": 15}
    lst = s.split(" ")
    start = next((int(item) - i for i, item in enumerate(lst) if item.isdecimal()), no_int.get(s))
    return list(range(start, start + len(lst)))
