def multiple_of_index(arr):
    """
        Returns a list of elements which are multiple of their own index in 'arr'.
    """
    return [element for index, element in enumerate(arr[1:], 1) if not element % index]
