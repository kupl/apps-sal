def first_tooth(some_list):
    answer_list = []
    if len(some_list) == 1:
        return some_list.index(max(some_list))
    else:
        answer_list.append(some_list[0] - some_list[1])
        for i in range(1, len(some_list) - 1):
            answer_list.append((some_list[i] - some_list[i - 1]) + (some_list[i] - some_list[i + 1]))
        answer_list.append(some_list[len(some_list) - 1] - some_list[len(some_list) - 2])
        if answer_list.count(max(answer_list)) > 1:
            return -1
        return answer_list.index(max(answer_list))

