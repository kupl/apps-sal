def extract_array(s):
    arr = s.split(' ')
    letters = []
    numbers = []
    index = 0
    while index < len(arr):
        temp_arr = []
        for letter in arr[index]:
            if(str.isdigit(letter)):
                temp_arr.append(letter)
            else:
                letters.append(letter+str(index))
        numbers.append(''.join(temp_arr))
        index += 1
    return numbers, letters

def sort_arr(item, sort_by):
    return [x for _,x in sorted(zip(sort_by, item))]

def do_math(s):
    nums = [int(x) for x in sort_arr(*extract_array(s))]
    index = 1
    result = nums[0]
    while index < len(nums):
        if(index % 4 == 1):
            result += nums[index]
        elif(index % 4 == 2):
            result -= nums[index]
        elif(index % 4 == 3):
            result *= nums[index]
        else:
            result /= nums[index]
        index += 1
    return round(result)
