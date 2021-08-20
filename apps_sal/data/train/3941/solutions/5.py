def reverse_fizzbuzz(string, start=0):

    def fb_gen(start=1):
        while True:
            if not (start % 5 or start % 3):
                yield (start, 'FizzBuzz')
            elif not start % 3:
                yield (start, 'Fizz')
            elif not start % 5:
                yield (start, 'Buzz')
            else:
                yield (start, start)
            start += 1
    str_split = string.split()
    for (i, v) in enumerate(str_split):
        if v.isdigit():
            return list(range(int(v) - i, len(str_split) + int(v) - i))
    (gen, index_check) = (fb_gen(), 0)
    for (ind, val) in gen:
        if str_split[index_check] == val:
            if index_check == len(str_split) - 1:
                return list(range(ind - len(str_split) + 1, ind + 1))
            index_check += 1
        else:
            index_check = 0
