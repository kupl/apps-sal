def isValid(formula):
     check1 = (1 in formula and 2 in formula)#should be false
     check2 = (3 in formula and 4 in formula) #should be false
     check3 = (5 in formula and 6 not in formula) #should be false
     check4 = (6 in formula and 5 not in formula) # should be false
     check5 = (7 in formula or 8 in formula) #should be true
     #check_list=[check1, check2, check]
     if check1==True or check2==True or check3==True or check4==True or check5==False :
        return False
     else:
        return True
