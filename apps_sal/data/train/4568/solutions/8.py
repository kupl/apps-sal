import random, math

# even if k is on the order of n, the average case is O(n)
# worst case is O(n^2)
def find_min_max_product(arr, k):
    if k < 1 or k > len(arr) or len(arr) == 0:
        return None
    
    # get k largest values (by absolute value)
    # and also construct a list of all the other values
    k_vals, other_vals = partition_around_k(arr, k, True)
        
    largest_product = 1
    smallest_positive_k_val = None
    smallest_negative_k_val = None
    # single loop through arr, so still O(n)
    for num in k_vals:
        # calculate the largest possible product by absolute value
        largest_product *= num
        # get the smallest positive and smallest negative values in k_vals
        if num > 0 and (smallest_positive_k_val == None or num < smallest_positive_k_val):
            smallest_positive_k_val = num
        if num < 0 and (smallest_negative_k_val == None or num > smallest_negative_k_val):
            smallest_negative_k_val = num
    
    # min and max are the same
    if k == len(arr):
        return largest_product, largest_product
    
    # if the largest product was positive: now find the largest negative product
    # if the largest product was negative: now find the largest positive product
    other_min_or_max = negate_product(arr, largest_product, smallest_negative_k_val, smallest_positive_k_val, other_vals)

    # if there was no way to flip the sign, instead find the smallest product by absolute value
    if other_min_or_max == None:
        # this mirrors the logic above, except with the seek_largest param flipped
        k_vals, other_vals = partition_around_k(arr, k, False)
        smallest_product = 1
        for num in k_vals:
            smallest_product *= num
        other_min_or_max = smallest_product

    # always return the min followed by max
    if largest_product > other_min_or_max:
        return other_min_or_max, largest_product
    else:
        return largest_product, other_min_or_max

# find the other min or max by flipping one of its factors from positive to negative or vice versa
def negate_product(arr, largest_product, smallest_negative_k_val, smallest_positive_k_val, other_vals):
    other_min_or_max = None
    need_min = largest_product > 0
    negate_removed = None
    positive_removed = None
    if smallest_negative_k_val != None:
        negate_removed = largest_product // smallest_negative_k_val
    if smallest_positive_k_val != None:
        positive_removed = largest_product // smallest_positive_k_val
    
    # single loop through arr, so still O(n)
    for num in other_vals:
        # calculate new possible product
        if num >= 0 and negate_removed != None:
            product = negate_removed * num
        elif num <= 0 and positive_removed != None:
            product = positive_removed * num
        else:
            continue
        
        # update the min or max
        if other_min_or_max == None:
            other_min_or_max = product
            continue
        is_product_better = product < other_min_or_max if need_min else product > other_min_or_max
        if is_product_better:
            other_min_or_max = product
            
    return other_min_or_max

# find k-th largest element, by distance from zero
# average case O(n), worst case is O(n^2)
def quick_select_absolute_k(arr, k, seek_largest):
    # base cases
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
    
    # everything remaining is duplicates
    if len(same) == len(arr):
        return arr[0]
    
    preferred_array = larger if seek_largest else smaller
    other_array = smaller if seek_largest else larger
    if len(preferred_array) >= k:
        return quick_select_absolute_k(preferred_array, k, seek_largest)
    else:
        return quick_select_absolute_k(other_array, k - len(preferred_array), seek_largest)

# change to median-of-medians to improve worst case from O(n^2) to O(n)
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
    # single loop through arr, so still O(n)
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
    
    # handling for duplicates
    remainder = k - len(k_vals)
    for i in range(remainder):
        k_vals.append(k_val_copies[i])
    for i in range(remainder, len(k_val_copies)):
        other_vals.append(k_val_copies[i])
    
    return k_vals, other_vals
