# # cook your dish here
# import string
# t= int(input())
# for i in range(t):
#     str_ = input()
    
#     while True:
#         for j in range(0, len(str_)-2):
#             if (str_[j]+str_[j+1]+str_[j+2]=="abc"):
#                 str_.replace(str[j], "")
#                 str_.replace(str[j+1], "")
#                 str_.replace(str[j+2], "")
#             else:
#                 continue
#         if 'abc' not in str_:
#             break
#         else:
#             continue
#     print(str_)


t = int(input())
for i in range(t):
    str_ = input()
    while True:
        if 'abc' in str_:
            str_= str_.replace('abc', '')
        else:
            break
    print(str_)

