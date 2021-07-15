def order_weight(strng):

    print(strng)
    def sum_strng(some_string):
        return sum(int(x) for x in some_string if x.isdigit())

    original_string_array = strng.split(' ')

    tuple_arr = []

    def order(arr):
        for i in arr:
            tuple_arr.append((i,sum_strng(i)))

    order(original_string_array)

    tuple_arr.sort(key=lambda tup: tup[0])
    tuple_arr.sort(key=lambda tup: tup[1])

    return ' '.join([x[0] for x in tuple_arr])
