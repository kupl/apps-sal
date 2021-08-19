def next_smaller(n):

    # Create a list of each digit in n
    numbers = [int(i) for i in str(n)]

    # Loop over each digit in the numbers list, from right to left
    for i in range(len(numbers) - 1, 0, -1):

        # If a number is less than the number to its left, split into 2 lists
        if numbers[i] < numbers[i - 1]:
            rearrange_list = numbers[i - 1:]  # numbers on the right of i -1
            original_list = numbers[:i - 1]  # numbers on the left of i -1
            less_than_values = []  # will contain possible substitutions for i -1

            # Loop over the rearrange_list
            for i in rearrange_list:

                # if the number is smaller than i, append it to less_than_values
                if i < rearrange_list[0]:
                    less_than_values.append(i)

            # Add the max value from less_than_values to the end of the original_list,
            # then add the rest of the sorted values from rearrange_list to the original_list
            original_list.append(max(less_than_values))
            rearrange_list.remove(max(less_than_values))
            original_list += sorted(rearrange_list, reverse=True)

            # Join the list together to get the output
            output = int(''.join([str(num) for num in original_list]))

            # If the output starts with 0, return -1. Otherwise, return the ouput.
            if len(str(output)) < len(str(n)):
                return -1
            else:
                return output

    # Return -1 if n is None, or if there are no smaller numbers
    return -1
