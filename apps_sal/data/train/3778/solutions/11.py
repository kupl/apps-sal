def find_smallest_int(arr):
    answer = arr[0]
    for nr in arr:
        if nr < answer:
            answer = nr
    return answer
