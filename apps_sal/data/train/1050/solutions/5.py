from sys import stdin, stdout 

def main():
    numberOfCases = int(stdin.readline())
    
    for i in range(0, numberOfCases):
        arr = [char for char in stdin.readline().strip()]
        starter = []
        count = 0
        currentCount = 0
        
        
        for element in arr:
            if element == "<":
                starter.append(element)
            else:
                if len(starter) == 0:
                    break
                starter.pop()
                
                if len(starter) == 0:
                    count = count + 2 + currentCount
                    currentCount = 0
                else :
                    currentCount += 2
        
        print(count)
                        
 
# call the main method
def __starting_point():
    main()    
__starting_point()
