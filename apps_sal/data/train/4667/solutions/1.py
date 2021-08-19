def traffic_jam(main_road, side_streets):
    answer = main_road
    for i in range(len(side_streets) - 1, -1, -1):
        ss = list(side_streets[i])[::-1]
        j = i + 1
        while ss:
            answer = answer[:j] + ss.pop(0) + answer[j:]
            j += 2
    return answer[:answer.find('X') + 1]
