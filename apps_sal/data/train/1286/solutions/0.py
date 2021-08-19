import math


def main():
    #print("enter i, k, s")
    IN = '11 6 5'
    z = IN.split()
    z = input().split()
    i = int(z[0])
    k = int(z[1])
    s = int(z[2])

    #print("enter a_i and b_i")
    IN = '4 5'
    z = IN.split()
    z = input().split()
    a_i = int(z[0])
    b_i = int(z[1])

    #print( "i = %d   k = %d   s = %d " % (i, k, s)  )
    #print( "a_i = %d   b_i = %d" % (a_i, b_i)  )

    x = math.sqrt(2)
    y = math.sqrt(3)
    # print(x,y)

    # Obtaining the k-th element when k >= i
    if(i <= k):
        diff = k - i
        # if both k and i are odd or even
        if(k - i) % 2 == 0:
            # print("#1")
            ans = (a_i + b_i) * math.pow(2, 2 * (k - i) - s)
            #diff = int(diff/2)
            #ans =  (a_i + b_i) * math.pow(2,4*diff-s)

        # if i and k are of different parities then obtaining first
        # a_(i+1) and b_(i+1)
        else:
            # print("#2")
            ans = (2 * x * a_i + 2 * x * y * b_i) * math.pow(2, 2 * (k - (i + 1)) - s)
            diff = int(diff / 2)
            ans = (2 * x * a_i + 2 * x * y * b_i) * math.pow(2, 4 * diff - s)
            #print("1: ", (2*x*a_i + 2*x*y*b_i))
            #print("2: ", math.pow(2,4*diff - 2- s))
            #print("2 sol: ", math.pow(2,4*int(diff)-s))
            #print("diff: ",diff)

    # Obtaining the k_th element when k < i
    else:
        diff = i - k
        # if both k and i are odd or even
        if(i - k) % 2 == 0:
            # print("#3")
            ans = (a_i + b_i) / math.pow(2, 2 * (i - k) + s)
            #diff =  int(diff/2)
            #ans =  (a_i + b_i) / math.pow(2,4*diff+s)

        # if i and k are of different parities then obtaining first
        # a_(i+1) and b_(i+1)
        else:
            # print("#4")
            ans = (2 * x * a_i + 2 * x * y * b_i) / math.pow(2, 2 * (i + 1 - k) + s)
            diff = int(diff / 2)
            ans = (2 * x * a_i + 2 * x * y * b_i) / math.pow(2, 4 * diff + 4 + s)

    print(ans)


main()
