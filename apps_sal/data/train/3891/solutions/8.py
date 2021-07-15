def get_new_notes(salary,bills):
    for bill in bills:
        salary -= bill
    return max(int(salary/5),0)
