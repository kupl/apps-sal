class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ptr1,ptr2,ptr3,ptr4=0,1,2,3
        time,maxtime = 0,0
        hour,mins = 0,0
        if arr == [0,0,0,0]:
            return \"00:00\"
        finalTime = \"\"
        valid = False
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        ptr1,ptr2,ptr3,ptr4=3,2,0,1
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        ptr1,ptr2,ptr3,ptr4=2,3,1,0
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        ptr1,ptr2,ptr3,ptr4=2,0,3,1
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        ptr1,ptr2,ptr3,ptr4=1,3,0,2
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        ptr1,ptr2,ptr3,ptr4=1,0,3,2
        for i in range(0,64):
            hour=arr[ptr1]*10+arr[ptr2]
            mins=arr[ptr3]*10+arr[ptr4]
            if(hour<24 and mins<60):
                time = hour*100+mins
                if(time>maxtime):
                    valid = True
                    maxtime = time
            if(ptr1>=3):ptr1 = 0 
            else: ptr1+=1
            if(ptr2>=3):ptr2 = 0 
            else: ptr2+=1
            if(ptr3>=3):ptr3 = 0 
            else: ptr3+=1
            if(ptr4>=3):ptr4 = 0 
            else: ptr4+=1
        finalTimeStr = str(maxtime)
        print(finalTimeStr)
        if(len(finalTimeStr)==3):
            finalTimeStr = \"0\" + finalTimeStr
        return finalTimeStr[0]+finalTimeStr[1]+\":\"+finalTimeStr[2]+finalTimeStr[3] if valid else \"\"
    
    
