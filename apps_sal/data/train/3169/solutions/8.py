vector = [0, 1, 1, 2, 4]
answers = [0, 1, 1, 1, 1]
for i in range(43996):
    vector = vector[1:] + [sum(vector)]
    answers.append(answers[-1] + vector[-1] % 2)


def count_odd_pentaFib(n):
    return answers[n]
