def whatday(num):
    return ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")[num-1] if 0<num<=7 else 'Wrong, please enter a number between 1 and 7'
