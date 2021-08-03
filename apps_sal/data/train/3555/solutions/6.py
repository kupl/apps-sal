def Hanoi_Solution(n):
    # Establish base cases
    if n == 0:
        return([[], [], []])
    if n == 1:
        return([[[1], [], []], [[], [], [1]]])
    # Setup recursion
    else:
        L = len(Hanoi_Solution(n - 1))
        # Move from [[n,..,1],[],[]] to [n,[n-1,...,1],[]]
        first_half = Hanoi_Solution(n - 1)
        for i in range(L):
            # Insert the new number at the beginning in the previous solution
            first_half[i][0].insert(0, n)
            # Switch the last two positions in each move
            temp_1 = first_half[i][2]
            first_half[i][2] = first_half[i][1]
            first_half[i][1] = temp_1
        # Move from [[],[n-1,...,1],[n]] to [[],[],[n,...,1]]
        second_half = Hanoi_Solution(n - 1)
        for i in range(L):
            # Insert the new number at the end in the previous solution
            second_half[i][2].insert(0, n)
            # Switch the first two positions in each move
            temp_2 = second_half[i][1]
            second_half[i][1] = second_half[i][0]
            second_half[i][0] = temp_2
        # Join the two halves into a single solution of length 2**n
        for i in second_half:
            first_half.append(i)
        return(first_half)

# Print the solution in the string format suggested


def hanoiArray(n):
    return((''.join(str(i) + '\n' for i in Hanoi_Solution(n)))[:-1])
