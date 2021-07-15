# def no_space(x):
#     i = 0
#     str_list = list(x)
#     while i < len(x):
#         if x[i] == " ":
#             x[i] = ""
#         i +=1
#     return x

def no_space(x):
    x = x.replace(" ","")
    return x
