def next_smaller(n):
    numbers = [int(i) for i in str(n)]
    for i in range(len(numbers) - 1, 0, -1):
        if numbers[i] < numbers[i - 1]:
            rearrange_list = numbers[i - 1:]
            original_list = numbers[:i - 1]
            less_than_values = []
            for i in rearrange_list:
                if i < rearrange_list[0]:
                    less_than_values.append(i)
            original_list.append(max(less_than_values))
            rearrange_list.remove(max(less_than_values))
            original_list += sorted(rearrange_list, reverse=True)
            output = int(''.join([str(num) for num in original_list]))
            if len(str(output)) < len(str(n)):
                return -1
            else:
                return output
    return -1
