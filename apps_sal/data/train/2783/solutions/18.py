import math 


def get_grade(a, b, c):
    mean = math.floor((a+b+c)/3)
    print(mean)
    grades = {'A': [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
              'B': [98, 88, 87, 86, 85, 84, 83, 82, 81, 80],
              'C': [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
              'D': [69, 68, 67, 66, 65, 64, 63, 62, 61, 60]}
    for k in grades:
        if mean in grades[k]:
            return k
    return 'F'

