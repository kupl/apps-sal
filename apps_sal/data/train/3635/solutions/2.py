def sflpf_data(val, nMax):
    # your code here
    # your code here
    prime = [2, 3]
    result = []
    head = 1
    tail = 0
    for i in range(4, nMax):
        i_temp = i
        for j in prime:
            if i == 1 or j > val:
                break
            while i % j == 0:
                i /= j
                if head == 0:
                    head = j
                tail = j
        if i == 1:
            if head + tail == val:
                result.append(i_temp)
        else:
            prime.append(i_temp)
        head = 0
    return result
