def sum_digits(number):
    t=0
    for i in str(number):
              if i.isdigit():
                  t =t +int(i)
    return t
