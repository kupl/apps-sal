def sum_array(arr):
    try:
        print(sorted(arr))
        print(sorted(arr)[1:-1])
        return sum(sorted(arr)[1:-1]) if len(arr) > 2 else 0
    except(TypeError):
        return 0
