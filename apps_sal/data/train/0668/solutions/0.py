def max_sum(arr):
    # Finds the maximum sum of sub-arrays of arr
    max_till_now = -1000000  # minimum possible number
    current_sum = 0
    for i in range(len(arr)):
        if current_sum < 0:
            # If sum of previous elements is negative, then ignore them. Start fresh
            # with `current_sum = 0`
            current_sum = 0

        current_sum += arr[i]

        # Update max
        if max_till_now < current_sum:
            max_till_now = current_sum

    return max_till_now


def solve(A, k):
    if k == 1:
        return max_sum(A)
    # Find sum of elements of A
    sum_A = 0
    for i in range(len(A)):
        sum_A += A[i]

    Max_Suffix_Sum = -1000000
    current = 0
    for i in range(len(A)):
        current += A[-i - 1]
        if current > Max_Suffix_Sum:
            Max_Suffix_Sum = current

    Max_Prefix_Sum = -1000000
    current = 0
    for i in range(len(A)):
        current += A[i]
        if current > Max_Prefix_Sum:
            Max_Prefix_Sum = current

    if sum_A <= 0:
        # Check two cases:

        # Case 1 : Check the max_sum of A
        case_1_max_sum = max_sum(A)

        # Case 2 : Check the max_sum of A + A
        case_2_max_sum = Max_Suffix_Sum + Max_Prefix_Sum

        # Return the maximum of the two cases
        return max([case_1_max_sum, case_2_max_sum])

    else:  # if sum_A > 0
        # Check two cases:

        # Case 1 : Check the max_sum of A
        case_1_max_sum = max_sum(A)

        # Case 2
        # Max sum = Max_Suffix_Sum + (k - 2)*sum_A + Max_Prefix_Sum

        case_2_max_sum = Max_Suffix_Sum + (k - 2) * sum_A + Max_Prefix_Sum

        # Return the maximum of the two cases
        return max([case_1_max_sum, case_2_max_sum])


# Main
T = int(input())  # No of test cases
for i in range(T):
    [N, k] = list(map(int, input().split(" ")))
    A = list(map(int, input().split(" ")))

    answer = solve(A, k)
    print(answer)
