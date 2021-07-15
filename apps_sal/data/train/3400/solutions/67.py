def even_numbers(arr,n):
    answer =[]
    for num in arr:
        if num % 2 == 0:
            answer.append(num)
    return answer[-n:]
