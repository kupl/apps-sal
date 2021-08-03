def enough(cap, on, wait):
    rem = cap - on
    if wait <= rem:
        return 0
    else:
        return wait - rem


a = enough(5, 3, 2)
if a == 0:
    print("Yes.Bob can take all passengers with him")
else:
    print(("Woops.Bob can't able to take ", a, " passengers into the bus"))
