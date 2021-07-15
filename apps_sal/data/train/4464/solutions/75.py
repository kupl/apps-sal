def feast(beast, dish):
    lower1= beast.lower()
    lower2= dish.lower()
    list1 = lower1[0]
    list2 = lower2[0]
    list3 = lower1[-1]
    list4 = lower2[-1]
    if list1 == list2 and list3 == list4:
        return True
    else:
        return False
