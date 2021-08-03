def reverse_fizzbuzz(s):
    arr = s.split(' ')
    if len(arr) == 1 and not arr[0].isdigit():
        return [3] if arr[0] == 'Fizz' else [5] if arr[0] == 'Buzz' else [15]

    def find_first_num(arr):
        for i in range(len(arr)):
            if arr[i].isdigit():
                return [int(i) * (-1), int(arr[i])]
        if arr[0] == 'Buzz':
            return [0, 5]
        return [0, 9]
    nu = find_first_num(arr)
    return [nu[0] + nu[1] + x for x in range(len(arr))]
