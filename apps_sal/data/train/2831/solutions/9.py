def largest_pair_sum(numbers): 
    # set swapped to true
    swapped = True
    # while loop if counter is not 1:
    while swapped:
        # set swapped to false and only stay in while loop if we swap in for loop
        swapped = False
        # loop thru nums using len of array - 1
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i + 1]:
                hold_value = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = hold_value
                swapped = True

    return numbers[-1] + numbers[-2]
