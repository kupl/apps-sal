def sort_array(source_array):

    return [] if len(source_array) == 0 else list(map(int,(','.join(['{}' if a%2 else str(a) for a in source_array])).format(*list(sorted(a for a in source_array if a%2 ==1))).split(',')))
