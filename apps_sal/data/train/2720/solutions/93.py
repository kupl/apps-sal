def solution(digits):

    def helper_func(item):
        temp = ''
        for i in item:
            temp = temp + str(i)
        return temp
    number_arr = [i for i in digits]
    result = [number_arr[i:i + 5] for i in range(0, len(number_arr) - 4)]
    string_res = [helper_func(i) for i in result]
    return max([int(i) for i in string_res])
