import itertools
def transpose_two_strings(arr):
    return '\n'.join( ' '.join(elt) for elt in itertools.zip_longest(arr[0],arr[1],fillvalue=' ') )
