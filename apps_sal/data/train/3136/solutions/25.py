def people_with_age_drink(age):
    return 'drink '+('toddy','coke','beer','whisky')[sum(not age<x for x in (14,18,21))]
