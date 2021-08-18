# List of generated elements
_elements = []


def _cgt(arr, pos):
    # Check if element isn't last
    # And element next to it is equal to 1(ONE)
    if pos + 1 < len(arr) and arr[pos + 1] == 1:
        # Check if current element is not bigger than previous one
        # Because we want to get sorted array
        # without repetitions
        if pos == 0 or arr[pos - 1] >= arr[pos] + 1:
            # If all conditions are met - creating new array
            # and calling recursive function with it
            _gt(arr[:pos] + [arr[pos] + 1] + arr[pos + 2:], pos)


def _gt(arr, pos):
    nonlocal _elements
    _elements.append(arr)  # Add current array of summands

    # Checking 2 elements
    # Example: For array [2, 1, 1] with pos = 0(zero) it will found:
    # array [3, 1] because 3 is first
    # and array [2, 2] because 2nd(second) number 2(two) is not bigger than first
    _cgt(arr, pos)
    _cgt(arr, pos + 1)

    # Exit function without return value
    return


# Function that returning array of summands for given number
def gt(num):
    nonlocal _elements
    # Clear elements array to get right result
    _elements = []
    # Start with array of 1s(ones) and position = 0(zero)
    _gt([1] * num, 0)
    # Return generated elements
    return _elements


def part(N):
    # Create new dictionary that will contain all products
    products = {}

    # Find product for each possible array of summands
    for arr in gt(N):
        prod = arr[0]
        for v in arr[1:]:
            prod *= v
        products[prod] = True

    # Sort found products to be able to find median
    pds = sorted(p for p in products)

    # Find values range
    r = pds[-1] - 1
    # Find average of array
    a = sum(pds) / float(len(pds))
    # Find array's median value
    m = (pds[len(pds) / 2] + pds[(len(pds) - 1) / 2]) / 2.0

    # Return formated info about sequence
    return 'Range: %i Average: %.2f Median: %.2f' % (r, a, m)
