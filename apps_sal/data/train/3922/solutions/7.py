def jumping(arr, n):
    pos = 0
    new_pos = 0
    answer = 0
    while True:
        try:
            new_pos = pos + arr[pos]
            if n > arr[pos]:
                arr[pos] += 1
            else:
                arr[pos] -= 1
            pos = new_pos
        except:
            for place in arr:
                if place == n:
                    answer += 1
            break
    return answer
