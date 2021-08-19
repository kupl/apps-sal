def set_alarm(employed, vacation):
    a = employed
    b = vacation

    if a == True:
        if b == False:
            return True
    if a == False:
        if b == False:
            return False
    if a == False and b == True:
        return False
    if a and b == True:
        return False


#     if a == True:
#         return True
#         if a and b == True:
#             return False
#     else:
#         return False
