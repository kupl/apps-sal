class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        total=2*n
        
        dicts={}
        
        for k in range(len(reservedSeats)):
            index=reservedSeats[k][0]
            val=reservedSeats[k][1]
            
            if index not in dicts:
                dicts[index]=[1,1,1];
            curr_list=dicts[index]
            maxim=max(curr_list[0]+curr_list[2],curr_list[1])
            if val in [2,3,4,5]:
                curr_list[0]=0
            if val in [4,5,6,7]:
                curr_list[1]=0
            if val in [6,7,8,9]:
                curr_list[2]=0
            dicts[index]=curr_list
            total=total-(maxim-max(curr_list[0]+curr_list[2],curr_list[1]))
        print(dicts)
        return total
        

