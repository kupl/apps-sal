def solve(n):
    min_cost = -1
    # Change the number to a string and reverse it.
    # This makes it possible to use .index to find the lowest place a digit appears.
    s = str(n)[::-1]
    # Calculate cost of each possible ending digit pair and keep the lowest cost at each point.
    for pair in ('00', '25', '50', '75'):
        cost = calculate_ending_pair_cost(s, pair)
        if min_cost == -1 or (cost != -1 and cost < min_cost):
            min_cost = cost

    return min_cost


def calculate_ending_pair_cost(s, pair):
    # First find the lowest place indices of each desired digit.
    indices = find_lowest_places(s, pair)
    # If we can't find one of the digits, then this ending pair is not possible.
    if indices is None:
        return -1
    # Start with an indicator of whether the desired digits are in the wrong order.
    cost = 1 if indices[1] > indices[0] else 0
    # Then swap the digits so the rest of our calculations are easier.
    # It's important to have these index numbers in descending order.
    if cost == 1:
        indices = (indices[1], indices[0])
    # Our number now looks something like this: aaa2bbbb5ccccc
    # The cost should be the number of digits (b's) we have to displace to move the 2 next to the 5,
    # and then twice the number of digits to displace to move the 2 and 5 to the "front".
    # This is because each c must move past both the 5 and the 2.
    cost += indices[0] - indices[1] - 1
    cost += 2 * indices[1]
    # We have one last special case to consider: What about leaving leading 0's in the high places?
    # We only bother with this if the number is more than 2 digits.
    if len(s) > 2:
        non_zero_index = first_non_zero_digit_after_indices(s, indices)
        if non_zero_index is None:
            return -1
        cost += len(s) - 1 - non_zero_index
        # Make sure not to double-count any digits we already moved as part of the desired digits.
        cost -= 1 if indices[0] > non_zero_index else 0
        cost -= 1 if indices[1] > non_zero_index else 0

    return cost


def find_lowest_places(s, pair):
    # Split the two-char string into the 1s place digit and 10s place digit.
    d10, d1 = pair
    try:
        i1 = s.index(d1)
    except:
        # Index raises an exception if it can't find the digit,
        # so just use that as an indicator of when to return a failure state.
        return None

    # If the pair we're looking for is a repeated digit ('00'), then we need to start
    # searching the string at the index just beyond that point.
    start = 0
    if d1 == d10:
        start = i1 + 1
    try:
        i10 = s.index(d10, start)
    except:
        return None

    return (i10, i1)


def first_non_zero_digit_after_indices(s, indices):
    # We need to reverse the string and indices because we're actually searching
    # from the highest place in the number now.
    s = s[::-1]
    indices = [len(s) - 1 - indices[i] for i in range(len(indices))]
    # Now search through linearly for the first non-zero digit which is not an index.
    non_zero_index = None
    for i in range(len(s)):
        if i not in indices and s[i] != '0':
            non_zero_index = i
            break
    # If we didn't find a non-zero index, that means we're dealing with something like
    # trying to use '25' as the final digits of 250. In other words, impossible.
    if non_zero_index is None:
        return None
    # Otherwise, translate the index back into place number.
    return len(s) - 1 - non_zero_index
