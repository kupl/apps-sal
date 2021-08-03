while True:
    a = input()
    if len(a):
        if a.isalnum():
            if len(a) == len(set(list(a))):
                print("Valid")
                break
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        break
