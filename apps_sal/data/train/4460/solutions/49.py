def whatday(num):
    nums=[1,2,3,4,5,6,7]
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
    d_o_w=dict(list(zip(nums,days)))
    if num in list(d_o_w.keys()):
        return d_o_w[num]
    else:
        return "Wrong, please enter a number between 1 and 7"

