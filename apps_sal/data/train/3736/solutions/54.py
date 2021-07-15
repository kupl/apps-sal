def minimum(arr):
    answer = arr[0]
    for i in arr:
        if i < answer:
            answer = i
    return answer

def maximum(arr):
    answer = arr[0]
    for i in arr:
        if i > answer:
            answer = i
    return answer
