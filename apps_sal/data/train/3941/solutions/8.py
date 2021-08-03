def reverse_fizzbuzz(string):
    arr = string.split()
    return list(map(lambda di: list(range(int(arr[di]) - di, int(arr[di]) - di + len(arr))), [next((k for k, v in enumerate(arr) if v.isdigit()), -1)]))[0] if any(a.isdigit() for a in arr) else [3] if string == 'Fizz' else [5] if string == 'Buzz' else [5, 6] if string == 'Buzz Fizz' else [9, 10] if string == 'Fizz Buzz' else [15]
