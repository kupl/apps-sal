def whatday(num):
    k = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    if num in list(k.keys()):
        return k[num]
    else:
        return 'Wrong, please enter a number between 1 and 7'
# Put your code here

