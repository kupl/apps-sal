class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#convert all times to minutes
#compile in a name based dictionary
#check who has violated the code
#return those names in alphabetical olrder
        mappedTimes = []
        for time in keyTime:
            mappedTimes.append(time_to_int(time))
        
        mydict = dict()
        for i in range(len(keyName)):
            if keyName[i] not in mydict:
                mydict[keyName[i]] = [mappedTimes[i]]
            else:
                mydict[keyName[i]].append(mappedTimes[i])
                
        for key in mydict:
            mydict[key] = sorted(mydict[key])
        
        rowdy_bois = []
        for name in mydict:
            max_counter = 0
            times = mydict[name]
            
            early_index = 0
            earliest_time = times[0]

            counter = 0
            for time in times:
                counter += 1
                if time-earliest_time <= 60:
                    if counter >= max_counter:
                        max_counter = counter
                else:
                    while time-earliest_time > 60:
                        early_index += 1
                        earliest_time = times[early_index]
                        counter -= 1
            print('{} had max counter {}'.format(name, max_counter))
            
            if max_counter >= 3:
                rowdy_bois.append(name)
                
        return sorted(rowdy_bois)
                
        
        

def time_to_int(time):
    time = time.split(\":\")
    return int(time[0]) * 60 + int(time[1])
    
