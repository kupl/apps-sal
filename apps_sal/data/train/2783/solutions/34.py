def get_grade(*args):
    avg , grades = sum(args)//len(args) , ['F' , 'D' , 'C' , 'B' , 'A','A']
    return grades[max(0 , (avg//10 - 5))]

