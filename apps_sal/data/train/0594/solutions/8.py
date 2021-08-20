def max_possible_sum_of_subsegment(array):
    current_max = 0
    maxx = 0
    for j in array:
        current_max += j
        if maxx < current_max:
            maxx = current_max
        if current_max < 0:
            current_max = 0
    return maxx


(n, x) = list(map(int, input().split()))
l = list(map(int, input().split()))
tot = sum(l)
maxx = max_possible_sum_of_subsegment(l)
print(tot - maxx + maxx / x)
