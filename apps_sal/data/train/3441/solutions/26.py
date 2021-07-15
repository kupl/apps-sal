def get_average(marks):
    sum=0
    for n in marks:
        sum=sum+n
    avg=sum//len(marks)
    return avg
