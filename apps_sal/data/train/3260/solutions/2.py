from itertools import permutations


def rearranger(k, *args):
    arguments = []
    numbers = []
    min_num = 10 ** 50
    for arg in [*args]:
        arguments.append(str(arg))
    for perm in permutations(arguments):
        num = int("".join(perm))
        if num % k == 0:
            if num == min_num and not perm in numbers:
                numbers.append(perm)
            if num < min_num:
                min_num = num
                numbers = [perm]

    if len(numbers) == 0:
        answer = "There is no possible rearrangement"
    elif len(numbers) == 1:
        nums = ', '.join(numbers[0])
        answer = f"Rearrangement: {nums} generates: {min_num} divisible by {k}"
    elif len(numbers) == 2:
        nums1 = ', '.join(numbers[0])
        nums2 = ', '.join(numbers[1])
        answer = f"Rearrangements: {nums1} and {nums2} generates: {min_num} divisible by {k}"
    return answer
