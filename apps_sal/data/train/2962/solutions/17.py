def divisible_by(numbers, divisor):
    var=[]
    for i in numbers:
        if i % divisor == 0:
            var.append(i)
    return var

