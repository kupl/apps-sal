t = int(input())
while t > 0:
    t = t - 1
    n, k = list(map(int, input().split()))
    a = [0] * n
    done = True

    def swap(z):
        for j in range(0, n):
            if a[j] == 0:
                a[j] = z
                done = True
                break
            else:
                if a[j] > z:
                    swap(j)
                    a[j] = z
                else:
                    done = False
                    break

    for i in range(0, n):
        for j in range(0, n):
            if abs(i - j) == k:
                if a[j] == 0:
                    a[j] = i + 1
                    done = True
                    break
                else:
                    if a[j] > i + 1:
                        swap(a[j])
                        a[j] = i + 1
                    else:
                        done = False

    if 0 in a:
        print('CAPTAIN AMERICA EVADES')
    else:
        if done:
            for c in a:
                print(c, end=' ')
            print()
        else:
            print('CAPTAIN AMERICA EVADES')

    # for i in range(1,n+1):
    #   if i - k >=0 :
    #       if a[abs(i-k-1)] == 0:
    #           a[abs(i-k-1)] = i
    #           done = True
    #       else:
    #           done = False
    #           break
    #   else:
    #       done = False
    #       break
    # if done:
    #   for c in a:
    #       print c,
    #   print
    # else:
    #   print "CAPTAIN AMERICA EVADES"
