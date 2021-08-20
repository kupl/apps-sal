def group(arr):
    (answer, brac, counter, already) = ([], [], 0, [])
    for i in arr:
        if arr.count(i) > 1 and i not in already:
            already.append(i)
            while counter < arr.count(i):
                counter += 1
                brac.append(i)
                if counter == arr.count(i):
                    answer.append(brac)
                    brac = []
                    counter = 0
                    break
        elif arr.count(i) == 1:
            answer.append([i])
    return answer
