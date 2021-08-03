def reverse_number(n):

    digits = 0
    num = 0
    if(n >= 0):
        num = n
        sign_n = 1
    else:
        num = -n
        sign_n = -1

    # while loop to count the number of digits, stored in digits
    while(num >= 1):
        num /= 10
        digits += 1

    # Debugging print statement
    # print("digits = " , digits)

    # Make n a positive number
    n = n * sign_n

    # for loop to store the digits of the positive part of n, strored as strings
    l_direct = list()
    for i in range(0, digits):
        l_direct.append(str(n % 10))
        n = int(n / 10)
        # print(n)
        i += 1

    # Concatenate the elements of the list into a string
    s = ""
    for j in range(0, digits):
        s = s + l_direct[j]

    # We need to account for the case of an empty string, otherwise python will complain if we try
    # to convert an empty string to an integer
    if(s == ''):
        result = 0
    else:
        # restore the original sign of n
        result = int(s) * sign_n

    return result
