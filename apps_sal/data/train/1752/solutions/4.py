from itertools import product

# Map a keypad number to the nearby numbers (including the number itself).
keypad_neighbors = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}

def get_pins(observed):
    # Build a 2D array of possibilities
    # Each row in the array is an entry
    # Each column is a possible number.
    pins = []
    for num in observed:
        pins.append(keypad_neighbors[num])
    
    # Generate every permutation of the possible numbers.
    for tup in product(*pins):
        yield ''.join(tup)
