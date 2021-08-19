import copy


def compute_problem_difficulty(problem, S):
    difficulty = 0
    for i in range(S - 1):
        if problem[i][1] > problem[i + 1][1]:
            difficulty += 1
    return difficulty


(P, S) = list(map(int, input().split()))
problem_difficulty = [[] for _ in range(30)]
i = 0
while i < P:
    subtasks_scores = list(map(int, input().split()))
    subtasks_num_of_contestants = list(map(int, input().split()))
    problem = []
    for j in range(S):
        problem.append([subtasks_scores[j], subtasks_num_of_contestants[j]])
    problem.sort()
    difficulty = compute_problem_difficulty(problem, S)
    problem_difficulty[difficulty].append(i + 1)
    i += 1
for i in range(30):
    j = 0
    while j < len(problem_difficulty[i]):
        print(problem_difficulty[i][j])
        j += 1
