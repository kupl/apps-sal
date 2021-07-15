def get_average(marks):
    media=0
    i=0
    for element in marks:
        i=i+1
        media=media+element
    media=media//i
    return media

