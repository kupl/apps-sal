T = int(input())
for test_cases in range(T):
    [N, M] = list(map(int, input().split(' ')))
    cost_single = list(map(int, input().split(' ')))

    class meal(object):

        def __init__(self, price, number, meal_list):
            self.cost = price
            self.num_meals = number
            self.meals = [0] * N
            for i in meal_list:
                self.meals[i - 1] = 1
            self.averageprice = price / number
    meal_sets = []
    for i in range(N):
        meal_sets.append(meal(cost_single[i], 1, [i + 1]))
    for i in range(M):
        line = input().split(' ')
        if int(line[0]) < sum((cost_single[j - 1] for j in map(int, line[2:]))):
            meal_sets.append(meal(int(line[0]), int(line[1]), list(map(int, line[2:]))))
    M = len(meal_sets) - N
    meal_sets = sorted(meal_sets, key=lambda meal_sets: meal_sets.averageprice)
    min_cost = [0]
    min_cost[0] = sum(cost_single)

    def selection(choice, index):
        this_cost = 0
        for i in range(N + M):
            this_cost += choice[i] * meal_sets[i].cost
        if this_cost >= min_cost[0]:
            return 0
        else:
            temp_list = []
            check_list = [0] * N
            for j in range(N + M):
                if choice[j] == 1:
                    temp_list.append(meal_sets[j].meals)
            check = 1
            if temp_list:
                for j in range(N):
                    check_list[j] = sum((row[j] for row in temp_list))
                    if check_list[j] == 0:
                        check = 0
                        break
                if check == 1:
                    min_cost[0] = this_cost
        if index == N + M - 2:
            selection(choice[0:index + 1] + [0], index + 1)
            selection(choice[0:index + 1] + [1], index + 1)
        elif index < N + M - 1:
            selection(choice[0:index + 1] + [0] + choice[index + 2:], index + 1)
            selection(choice[0:index + 1] + [1] + choice[index + 2:], index + 1)
    selection([0] * (N + M), 0)
    selection([1] + [0] * (N + M - 1), 0)
    print(min_cost[0])
