def largest_pair_sum(numbers): 
    largest=-10000
    for nums in numbers:
        if nums>largest:
            largest=nums
    second_largest=-10000
    numbers.remove(largest)
    for nums in numbers:
        if nums>second_largest:
            second_largest=nums
    return largest+second_largest
