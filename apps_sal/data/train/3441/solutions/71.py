import math


def get_average(marks):
    soma = 0
    if len(marks) > 0:
        for i in marks:
            soma += i
        media = soma / len(marks)
        return math.floor(media)


print(get_average([1, 2]))
