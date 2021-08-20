from itertools import permutations


def ssc_forperm(arr):
    maximum = -999999999
    minimum = 999999999
    total_score = [{'total perm': 0}, {'total ssc': 0}, {'max ssc': 0}, {'min ssc': 0}]
    lend = len(set(list(permutations(arr))))
    permutated_list = list(set(permutations(arr)))
    for element in permutated_list:
        temp = 0
        for (e, i) in enumerate(element, start=1):
            temp += e * i
        total_score[1]['total ssc'] += temp
        if temp > maximum:
            maximum = temp
            total_score[2]['max ssc'] = maximum
        if temp < minimum:
            minimum = temp
            total_score[3]['min ssc'] = minimum
    total_score[0]['total perm'] = lend
    return total_score
