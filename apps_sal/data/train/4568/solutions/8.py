import random
import math


def find_min_max_product(arr, k):
    if k < 1 or k > len(arr) or len(arr) == 0:
        return None

    k_vals, other_vals = partition_around_k(arr, k, True)

    largest_product = 1
    smallest_positive_k_val = None
    smallest_negative_k_val = None
    for num in k_vals:
        largest_product *= num
        if num > 0 and (smallest_positive_k_val == None or num < smallest_positive_k_val):
            smallest_positive_k_val = num
        if num < 0 and (smallest_negative_k_val == None or num > smallest_negative_k_val):
            smallest_negative_k_val = num

    if k == len(arr):
        return largest_product, largest_product

    other_min_or_max = negate_product(arr, largest_product, smallest_negative_k_val, smallest_positive_k_val, other_vals)

    if other_min_or_max == None:
        k_vals, other_vals = partition_around_k(arr, k, False)
        smallest_product = 1
        for num in k_vals:
            smallest_product *= num
        other_min_or_max = smallest_product

    if largest_product > other_min_or_max:
        return other_min_or_max, largest_product
    else:
        return largest_product, other_min_or_max


def negate_product(arr, largest_product, smallest_negative_k_val, smallest_positive_k_val, other_vals):
    other_min_or_max = None
    need_min = largest_product > 0
    negate_removed = None
    positive_removed = None
    if smallest_negative_k_val != None:
        negate_removed = largest_product // smallest_negative_k_val
    if smallest_positive_k_val != None:
        positive_removed = largest_product // smallest_positive_k_val

    for num in other_vals:
        if num >= 0 and negate_removed != None:
            product = negate_removed * num
        elif num <= 0 and positive_removed != None:
            product = positive_removed * num
        else:
            continue

        if other_min_or_max == None:
            other_min_or_max = product
            continue
        is_product_better = product < other_min_or_max if need_min else product > other_min_or_max
        if is_product_better:
            other_min_or_max = product

    return other_min_or_max


def quick_select_absolute_k(arr, k, seek_largest):
    if len(arr) == 1:
        return arr[0]
    if k == 1:
        return find_absolute_extreme(arr, seek_largest)

    pivot_index = pick_pivot_index(arr, 0, len(arr) - 1)
    smaller = []
    larger = []
    same = []
    for num in arr:
        if abs(num) < abs(arr[pivot_index]):
            smaller.append(num)
        elif abs(num) > abs(arr[pivot_index]):
            larger.append(num)
        else:
            if seek_largest:
                larger.append(num)
            else:
                smaller.append(num)
            same.append(num)

    if len(same) == len(arr):
        return arr[0]

    preferred_array = larger if seek_largest else smaller
    other_array = smaller if seek_largest else larger
    if len(preferred_array) >= k:
        return quick_select_absolute_k(preferred_array, k, seek_largest)
    else:
        return quick_select_absolute_k(other_array, k - len(preferred_array), seek_largest)


def pick_pivot_index(arr, min, max):
    return random.randint(min, max)


def find_absolute_extreme(arr, seek_largest):
    extreme = None
    for num in arr:
        if extreme == None:
            extreme = num
        elif seek_largest and abs(extreme) < abs(num):
            extreme = num
        elif not seek_largest and abs(extreme) > abs(num):
            extreme = num
    return extreme


def partition_around_k(arr, k, seek_largest):
    k_val = quick_select_absolute_k(arr, k, seek_largest)
    k_vals = []
    k_val_copies = []
    other_vals = []
    for num in arr:
        if abs(num) > abs(k_val):
            if seek_largest:
                k_vals.append(num)
            else:
                other_vals.append(num)
        elif abs(num) < abs(k_val):
            if seek_largest:
                other_vals.append(num)
            else:
                k_vals.append(num)
        else:
            k_val_copies.append(num)

    remainder = k - len(k_vals)
    for i in range(remainder):
        k_vals.append(k_val_copies[i])
    for i in range(remainder, len(k_val_copies)):
        other_vals.append(k_val_copies[i])

    return k_vals, other_vals
