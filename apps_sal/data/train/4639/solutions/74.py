powers = []
for i in range(0, 150):
    y = 2**i
    powers.append(y)

def power_of_two(x):
    if x == 0:
        return False
    

    elif x in powers:
        return True
    else:
        return False
  # your code here

