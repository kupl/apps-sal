import heapq


def min_value(digits):
    lista = []
    output = []
    for i in digits:
        if i not in lista:
            lista.append(i)
    heap = heapq.nsmallest(99, lista)
    heap_string = [str(i) for i in heap]
    convert = ''.join(heap_string)
    return int(convert)
