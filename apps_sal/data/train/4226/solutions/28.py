def remove_smallest(numbers):
    return (lambda x: x and x.remove(min(x)) or x)(numbers[:])
