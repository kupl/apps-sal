def whatday(num):
    dic = {"Sunday": 1,
           "Monday": 2,
           "Tuesday":3,
           "Wednesday": 4,
           "Thursday" : 5,
           "Friday" : 6,
           "Saturday" : 7,}
    for key, value in list(dic.items()):
        if dic[key] == num and num <= 7:
            return key
    return 'Wrong, please enter a number between 1 and 7'

# test.assert_equals(whatday(1), 'Sunday')
# test.assert_equals(whatday(2), 'Monday')
# test.assert_equals(whatday(3), 'Tuesday')

