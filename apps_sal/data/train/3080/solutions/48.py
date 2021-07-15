def who_is_paying(name):
    if len(name) < 3: return [name]
    else:
        first_two = name[0:2]
        return [name, first_two]
    
    
    
# Test.assert_equals(who_is_paying("Mexico"),["Mexico", "Me"])
# Test.assert_equals(who_is_paying("Melania"),["Melania", "Me"])
# Test.assert_equals(who_is_paying("Melissa"),["Melissa", "Me"])
# Test.assert_equals(who_is_paying("Me"),["Me"])
# Test.assert_equals(who_is_paying(""), [""])
# Test.assert_equals(who_is_paying("I"), ["I"])

