from datetime import datetime

class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        
        \"\"\"
        put everyone into a dictionary
        \"daniel contains times x\"
        \"alice contains times y\"
        
        iterate through each person and determine if their times are strange
        
        \"\"\"
        alerted = []
        namesTimes = {}
                
        for i in range(len(keyName)):
            if keyName[i] in namesTimes:
                namesTimes[keyName[i]].append(keyTime[i])
                namesTimes[keyName[i]].sort()
            else:
                namesTimes[keyName[i]] = [keyTime[i]]
                
        
        lowerbound = datetime.strptime('00:00','%H:%M') - datetime.strptime('00:00','%H:%M')
        upperbound = datetime.strptime('01:01','%H:%M') - datetime.strptime('00:00','%H:%M')
        
        
        for person, times in namesTimes.items():
            if len(times) >= 3:
                # only check if they even used their card 3 or more times
                # examine the times
                # how do we do that?
                # check the first 2. if they're within the same hour, check the first and third one
                #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                
                
                # let's make this inner loop more efficient: 
                # if the first two times don't qualify, increment x by 2
                # if the first and third times don't qualify, increment x by 3
                 for x in range(len(times)-2):
                    time1 = datetime.strptime(times[x], '%H:%M')
                    time2 = datetime.strptime(times[x+1], '%H:%M')

                    diff1 = time2 - time1
                    # if the first two times are within the hour, check the third time

                    if diff1 > lowerbound and diff1 < upperbound:
                        # we can check the third time, then

                        print(\"for\", person, \"differences of\", diff1)

                        time3 = datetime.strptime(times[x+2], '%H:%M')

                        diff2 = time3 - time1

                        if diff2 > lowerbound and diff2 < upperbound:
                            print(\"for\", person, \"differences of\", diff2)
                            # we found someone
                            alerted.append(person)
                            # go to the next person
                            break  
        print(alerted)
        alerted.sort()
        return alerted
                    

                
        
#   for x in range(len(times)-2):
#                     time1 = datetime.strptime(times[x], '%H:%M')
#                     time2 = datetime.strptime(times[x+1], '%H:%M')

#                     diff1 = time2 - time1
#                     # if the first two times are within the hour, check the third time

#                     if diff1 > lowerbound and diff1 < upperbound:
#                         # we can check the third time, then

#                         print(\"for\", person, \"differences of\", diff1)

#                         time3 = datetime.strptime(times[x+2], '%H:%M')

#                         diff2 = time3 - time1

#                         if diff2 > lowerbound and diff2 < upperbound:
#                             print(\"for\", person, \"differences of\", diff2)
#                             # we found someone
#                             alerted.append(person)
#                             # go to the next person
#                             break              
        
