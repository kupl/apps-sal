def countOnes(left, right):
    """
    Each number has a particular number of digits in its binary representation.
    There are sets of numbers with the same number of digits in their binary representation.
    For example there is a set of 4-digit-numbers: 8,9,10,11,12,13,14,15.

    num | binary representation
      8 | 1 0 0 0
      9 | 1 0 0 1
     10 | 1 0 1 0
     11 | 1 0 1 1
     12 | 1 1 0 0
     13 | 1 1 0 1
     14 | 1 1 1 0
     15 | 1 1 1 1

    That kind of sets of n-digit numbers we will call 'blocks'.
    For whole blocks we can easily calculate sum of ones with the formula 2^(n-1) * (1 + 0.5*(n-1))
    But 'left' and 'right' digits can be somewhere inside of their blocks, so we have to sum only part of ones in block.

    For example, in case of range <10, 35> we have to split our calculation in 3 parts:
    1) Sum of the incomplete 4-digit-block, which contains number 10.
    Number 10 splits that block on two parts and we sum ones only from second part (for numbers 10-15).
    2) Sum of 5-digit-block (ones in numbers: 16-31)
    3) Sum of the incomplete 6-digit-block, which contains number 35.
    Number 35 splits that block on two parts and we sum ones only from first part (for numbers 32-35).

    :return: sum of ones in binary representation of all numbers in range <left, right>
    """
    left_binary_digits = count_binary_digits(left)
    right_binary_digits = count_binary_digits(right)
    right_binary_sum = sum([int(i) for i in str(bin(right))[2:]])
    left_position_in_block = left - calculate_starting_digit(left_binary_digits) + 1
    right_position_in_block = right - calculate_starting_digit(right_binary_digits) + 1
    if left_binary_digits == right_binary_digits:
        number_of_ones = calculate_ones_in_incomplete_block(left_binary_digits, left_position_in_block) - calculate_ones_in_incomplete_block(right_binary_digits, right_position_in_block) + right_binary_sum
    else:
        number_of_ones = calculate_ones_in_incomplete_block(left_binary_digits, left_position_in_block) + calculate_multiple_blocks(left_binary_digits + 1, right_binary_digits - 1) + calculate_ones_in_incomplete_block(right_binary_digits, right_position_in_block, True) + right_binary_sum
    return number_of_ones


def count_binary_digits(number):
    """:return: number of digits in binary representation of integer"""
    return len(str(bin(number))) - 2


def calculate_starting_digit(n_digits):
    """
    We know, that the block of n-digits-numbers contains of 2^(n-1) numbers
    To calculate first number of 4-digits-block we have to count numbers from previous blocks and add 1:
    2^(1-1) + 2^(2-1) + 2^(3-1) + 1 = 1 + 2 + 4 + 1 = 8
    :return: first number of n_digits-block
    """
    return sum([pow(2, i - 1) for i in range(1, n_digits)]) + 1


def calculate_ones_in_incomplete_block(n_digits, position, front_part=False):
    """
    We use of following properties:
    - First column of block is always filled with ones.
    - Second column contains of dwo parts: half column of zeroes and half column of ones.
        If we split next column in half, each part will follow above pattern.
        If we split next column into four pieces, each part will follow the same pattern from second column and so on.

    We iterate through consecutive columns, moving 'middle_row' indicator as we split columns in smaller parts.
    As we calculating second part of block, we add all ones under our indicator (including one on indicator) and ommit ones above.

    :param n_digits: number of digits in binary representation
    :param position: position of number in n_digits-block
    :param front_part: indicates whether we calculate normally ('second part' of block - from position to the end)
            or we subtract second part from sum of ones in whole block and return 'first part'
    :return: In block split in two parts by position we return sum of one form second or first part
    """
    all_rows = pow(2, n_digits - 1)
    upper_ones = 0
    last_row = all_rows
    result = last_row - position + 1
    middle_row = last_row / 2
    for i in range(n_digits - 1):
        if position <= middle_row:
            result += all_rows / 2 - upper_ones
            temp = int(last_row)
            last_row = middle_row
            middle_row -= (temp - middle_row) / 2
        else:
            result += last_row - position + 1 + (all_rows - last_row) / 2
            upper_ones += (last_row - middle_row) / 2
            middle_row += (last_row - middle_row) / 2
    if front_part:
        return all_rows * (1 + 0.5 * (n_digits - 1)) - result
    else:
        return result


def calculate_multiple_blocks(digits_start, digits_stop):
    """
    :return: sum of ones in all block from digits_start-block to digits_stop-block
    """
    result = 0
    if digits_stop >= digits_start:
        for i in range(digits_start, digits_stop + 1):
            result += pow(2, i - 1) * (1 + 0.5 * (i - 1))
    return result
