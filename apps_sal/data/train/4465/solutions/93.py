def super_size(n):
    """Function that rearranges an integer into its largest possible value.
    :param int n
        integer to rearranges
    """
    number_list = list(str(n))
    number_list.sort(reverse=True)
    return int(''.join(number_list))
