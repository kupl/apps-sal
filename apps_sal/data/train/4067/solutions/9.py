def iq_test(numbers):
    even, odd = [], []
    new_nums = numbers.split()
    for index, num in enumerate(new_nums,1):
        if int(num) % 2 == 0:
            even.append(index)
        else:
            odd.append(index)
      
    if len(even) > len(odd):
        return int(odd[0])
    else:
        return int(even[0])
