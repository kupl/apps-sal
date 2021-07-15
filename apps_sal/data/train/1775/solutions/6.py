#Solving the grid can be broken down into the following main steps:
#1) Using the outside view to remove certain options or place known numbers
#2) Look for block that only has one remaining option (step repeated each time grid is adjusted)
#3) Look for lines with two blocks with restriction of two same options remove these options for other blocks in line
#3) Look for lines with 2 blocks remaining. Create 2 options from these and compare to the view from both sides

#Practical routes taken:
#1)gridComplete is an array used to indicate if number was placed or not. This helps confirm if number is "placed" or just last remaining option. As when it is placed the same number needs to be removed from line and adjacent line
#2)Clues where placed into array with pairs horizonal and vertical. So that the can be looped and assigned easily

import numpy as np

def solve_puzzle (clues):
    
    nonlocal grid
    grid = np.array([("1234","1234","1234","1234"),("1234","1234","1234","1234"),("1234","1234","1234","1234"),("1234","1234","1234","1234")])
    
    nonlocal gridComplete
    gridComplete = np.array([(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)])
    
    nonlocal cluesN
    cluesN = list(map(str,clues))
    clues = list(map(str,clues))
    
    nonlocal hor
    nonlocal vert
    hor = [(clues[0]+clues[11]),(clues[1]+clues[10]),(clues[2]+clues[9]),(clues[3]+clues[8])]
    vert =[(clues[15]+clues[4]),(clues[14]+clues[5]),(clues[13]+clues[6]),(clues[12]+clues[7])]
    
#1) Removing known options and placing according to view and standard practise
#----------------------------------------------------------------------------
    #1: M1:
    #    -1 place 4
    #    -4 place 1234
    #    -2V remove [1] 3
    #    -2V remove [0] 4
    #    -3V remove [0] 3
    
    #M1 - 4 place 1234
    for z in range(len(cluesN)):
        if cluesN[z] == "4" and z<=3:
            placeNum(1,0,z, check = False)
            placeNum(2,1,z, check = False)
            placeNum(3,2,z, check = False)
            placeNum(4,3,z, check = False)
        elif cluesN[z] =="4" and 4 <= z <= 7:
            placeNum(1,z-4,3, check = False) 
            placeNum(2,z-4,2, check = False)
            placeNum(3,z-4,1, check = False)
            placeNum(4,z-4,0, check = False)
        elif cluesN[z] == "4" and 8 <= z <= 11:
            placeNum(1,3,11-z, check = False)  # changed this from placeNum(4,11-z,3)
            placeNum(2,2,11-z, check = False)
            placeNum(3,1,11-z, check = False)
            placeNum(4,0,11-z, check = False)
        elif cluesN[z] == "4" and 12 <= z <= 15:
            placeNum(1,15-z,0, check = False)
            placeNum(2,15-z,1, check = False)
            placeNum(3,15-z,2, check = False)
            placeNum(4,15-z,3, check = False)
            
        #M1 - 1 place 4
        if cluesN[z] == "1" and z<=3:
            placeNum(4,0,z, check = False)
        elif cluesN[z] =="1" and 4 <= z <= 7:
            placeNum(4,z-4,3, check = False) 
        elif cluesN[z] == "1" and 8 <= z <= 11:
            placeNum(4,3,11-z, check = False) 
        elif cluesN[z] == "1" and 12 <= z <= 15:
            placeNum(4,15-z,0, check = False)

    #M1 - 2v remove[1] 3 
    removeM1(2,1,3)
    
    #M1 - 2V remove [0] 4
    removeM1(2,0,4)
    
    #M1 - 3V remove [0] 3
    removeM1(3,0,3)
    
#-------------------------------------------------------------------
    
#2) - Check if any single options are left in a cell
    lookforsingle()
    
#3) - look for any paired options in a line and remove that pair from other cells
    double2()

#4) look for 2 cells left in line and create 2 options and compare to view
    lookforspace2() #one direction
    lookforspace2REV() #Reverse direction
    
    #Convert string to int in list for return
    grid = grid.astype(np.integer)
    #Return truple answer
    return tuple(map(tuple, grid))

def lookforspace2():
    
    #Look for 2 unknown cells calculate options and compare to view
    
    first = True
    first2 = True
    for y in range(4):
        view = vert[y][0]   #VIEW on left
        view1 = hor[y][0]   #VIEW from top
        lstOption1 = np.copy(grid[y])
        lstOption2 = np.copy(grid[y])
        lstVertOption1 = np.copy(grid[::,y])
        lstVertOption2 = np.copy(grid[::,y])
        
        for x in range(4):
            
            #horizontal check
            if len(str(lstOption1[x])) == 2:
    
                #remove first paired number and then the next remove second
                if first == True: 
                    optionPair = str(lstOption1[x])
                    lstOption2[x] = (str(lstOption2[x])).replace(str(optionPair[0]),"") 
                    lstOption1[x] = (str(lstOption1[x])).replace(str(optionPair[1]),"")
                    first = False
                elif first == False: 
                    lstOption1[x] = str(lstOption1[x]).replace(optionPair[0],"")
                    lstOption2[x] = str(lstOption2[x]).replace(optionPair[1],"")
                    first = True
                
            #Vertical check
            if len(str(lstVertOption1[x])) == 2:
    
                #remove first paired number and then the next remove second
                if first2 == True: 
                    optionPair2 = str(lstVertOption1[x])
                    lstVertOption2[x] = (str(lstVertOption2[x])).replace(str(optionPair2[0]),"") 
                    lstVertOption1[x] = (str(lstVertOption1[x])).replace(str(optionPair2[1]),"")
                    first2 = False
                elif first2 == False: 
                    lstVertOption1[x] = str(lstVertOption1[x]).replace(optionPair2[0],"")
                    lstVertOption2[x] = str(lstVertOption2[x]).replace(optionPair2[1],"")
                    first2 = True
        
        #calculate the view of each option
        calc1 = viewCalc(lstOption1.tolist())   
        calc2 = viewCalc(lstOption2.tolist())
        calc3 = viewCalc(lstVertOption1.tolist())
        calc4 = viewCalc(lstVertOption2.tolist())
        
        #if option correct then place option in grid
        if int(calc3) == int(view1) and int(calc3) != int(calc4):
            grid[::,y] = lstVertOption1
                #place answer
        elif int(calc4) == int(view1) and int(calc3) != int(calc4):
            grid[::,y] = lstVertOption2
        
        if int(calc1) == int(view) and int(calc1) != int(calc2):
            grid[y] = lstOption1
                #place answer
        elif int(calc2) == int(view) and int(calc1) != int(calc2):
            grid[y] = lstOption2
    
    lookforsingle() #clear out placed numbers from adjacent lines

def lookforspace2REV():
    
    #Look for 2 unknown cells calculate options and compare to view
    #Reversed direction
    
    first = True
    first2 = True
    for y in range(4):
        view = vert[y][1]   #VIEW on right
        view1 = hor[y][1]   #VIEW from bottom
        lstOption1 = (np.copy(grid[y]))[::-1]
        lstOption2 = (np.copy(grid[y]))[::-1]
        lstVertOption1 = (np.copy(grid[::,y]))[::-1]
        lstVertOption2 = (np.copy(grid[::,y]))[::-1]
        
        for x in range(4):
            
            if len(str(lstOption1[x])) == 2:
    
                #remove first and then the next remove second
                if first == True: 
                    optionPair = str(lstOption1[x])
                    lstOption2[x] = (str(lstOption2[x])).replace(str(optionPair[0]),"") 
                    lstOption1[x] = (str(lstOption1[x])).replace(str(optionPair[1]),"")
                    first = False
                elif first == False: 
                    lstOption1[x] = str(lstOption1[x]).replace(optionPair[0],"")
                    lstOption2[x] = str(lstOption2[x]).replace(optionPair[1],"")
                    first = True
                
            if len(str(lstVertOption1[x])) == 2:
    
                #remove first and then the next remove second
                if first2 == True: 
                    optionPair2 = str(lstVertOption1[x])
                    lstVertOption2[x] = (str(lstVertOption2[x])).replace(str(optionPair2[0]),"") 
                    lstVertOption1[x] = (str(lstVertOption1[x])).replace(str(optionPair2[1]),"")
                    first2 = False
                elif first2 == False: 
                    lstVertOption1[x] = str(lstVertOption1[x]).replace(optionPair2[0],"")
                    lstVertOption2[x] = str(lstVertOption2[x]).replace(optionPair2[1],"")
                    first2 = True
        
        calc1 = viewCalc(lstOption1.tolist())   #grid list row
        calc2 = viewCalc(lstOption2.tolist())
        calc3 = viewCalc(lstVertOption1.tolist())
        calc4 = viewCalc(lstVertOption2.tolist())
        
        if int(calc3) == int(view1) and int(calc3) != int(calc4):
            grid[::,y] = lstVertOption1[::-1]
        elif int(calc4) == int(view1) and int(calc3) != int(calc4):
            grid[::,y] = lstVertOption2[::-1]
        
        if int(calc1) == int(view) and int(calc1) != int(calc2):
            grid[y] = lstOption1[::-1]
        elif int(calc2) == int(view) and int(calc1) != int(calc2):
            grid[y] = lstOption2[::-1]
            
    
    lookforsingle()


    
def removeM1(viewpos, coord, removeNum):
    
    #Given a coordinate as location from the viewpos (viewpoint outside of grid linked to clues)
    #remove the option(removeNum) from the list
    
    lstCord = []
    for z in range(len(cluesN)):
        if cluesN[z] == str(viewpos):
            if z <= 3: lstCord = [coord,z]
            if 4 <= z <= 7: lstCord = [z-4,3-coord] 
            if 8 <= z <= 11: lstCord = [3-coord,11-z] 
            if 12 <= z <= 15: lstCord = [15-z,coord] 
            
            grid[lstCord[0]][lstCord[1]] = str(grid[lstCord[0]][lstCord[1]]).replace(str(removeNum),"")
    
        
def double2():
    
    #look for two pairs in line and remove from other options in adjacent lines
    
    dbl = False
    for y in range(4):
        for x in range(4):
            lst = gridComplete.sum(axis = 1)
            if len(grid[y][x]) == 2:
                for x2 in range(x+1,4):
                    if grid[y][x] == grid[y][x2]:
                        
                        for g in range(4):
                            try:
                                if len(str(grid[y][g])) > 1 and str(grid[y][g]) !=  grid[y][x2]: #already they are equal and checked that is 2
                                    grid[y][x2]= str(grid[y][x2]).replace((str(grid[y][x]))[0],"")
                                    dbl = True
                            except:
                                pass
                            try:
                                if len(str(grid[y][g])) > 1 and str(grid[y][g]) !=  grid[y][x2]: 
                                    grid[y][x2]= str(grid[y][x2]).replace((str(grid[y][x]))[1],"")
                                    dbl = True
                            except:
                                pass
                            
    if dbl == True:
        lookforsingle()
        double2()
    
def lookforsingle():
    #Look for single option in cell or where only one occurance of that option in line and place it
    count = 0
    pos = []
    placed = False
    posC = np.array([(0,0),(0,0),(0,0),(0,0)])
    countC=[0,0,0,0]
    for p in range(1,5):
        for a in range(4):
            if placed == False: 
                for o in range(4):
                    if str(p) in str(grid[a][o]) and len(str(grid[a][o])) > 1 and gridComplete[a][o] == 0:
                        count += 1
                        countC[a] = countC[a] + 1
                        posC[a] = [a,o]
                        pos = [a,o]
                        
                    elif len(str(grid[a][o])) == 1 and gridComplete[a][o] == 0:
                        placeNum(str(grid[a][o]), a, o,check = False)
                        placed = True
                        break
        
                if count == 1 and placed == False:
                    placeNum(p, pos[0], pos[1], check = False)
                    placed = True
                    break
                count == 0
        
        #coloumb single occurances
        for u in range(4):
            if placed == True: 
                break
            if countC[u] == 1:
                placeNum(p,posC[u][0],posC[u][1], check = False)
                placed = True
                
        countC = [0,0,0,0]
    
    if placed == True: lookforsingle()
        
    

def viewCalc(lstCalc): #provide a list of 4 integers
    
    #return the a calculation of amount of building can be seen from list
    
    prev = 0
    count = 0
    for i in range(4):
        if int(lstCalc[i]) > prev:
            count += 1
            prev = int(lstCalc[i])
    return count
        
def placeNum(num ,ypos, xpos, check = True):

    #places given number in coordinates of grid and then removes these options from
    #adjacent lines.
    #after which can be checked for single options left or not checked for placements to continue before checking
    
    for y in range(4):
        try:
            if len(str(grid[ypos][y])) > 1: grid[ypos][y]= str(grid[ypos][y]).replace(str(num),"") 
        except:
            pass
        try:
            if len(str(grid[y][xpos])) > 1: grid[y][xpos]= str(grid[y][xpos]).replace(str(num),"")
        except:
            pass
            
    grid[ypos][xpos] = num
    gridComplete[ypos][xpos] = 1
    if check == True:lookforsingle()

