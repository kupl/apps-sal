for O in range(int(input())):
    LA, BA = map(int, input().split())
    A, C = 1, 0
    while(True):
        if(LA >= A):
            LA -= A
            A += 1
            C += 1
        else:
            break
        if(BA >= A):
            BA -= A
            A += 1
            C += 1
        else:
            break
    if(C % 2 != 0):
        print("Limak")
    else:
        print("Bob")
