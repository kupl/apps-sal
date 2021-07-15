from math import floor

def get_average(marks):
    media = sum(marks)/len(marks)
    return floor(media)
