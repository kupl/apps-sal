import random
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.down=None
    
class Skiplist:

    def __init__(self):
        self.levels=[Node(-1) for i in range(16)]
        for i in range(0,15):
            self.levels[i].down=self.levels[i+1]
        self.maxlevel=1
        self.arr=[]
    
    def coinflip(self):
        a=random.random()>0.5
        return a
    
    def searchpath(self,value):
        m=self.maxlevel
        self.arr=[]
        for i in range(16):
            self.arr.append(self.levels[i])
        curlevelhead=self.levels[0]
        # print(\"value\",value)
        i=0
        while(i<16):
            
            while(curlevelhead):
                if curlevelhead.val<value:
                    # print(\"check\",i,curlevelhead.val,curlevelhead.down)
                    self.arr[i]=curlevelhead
                    prev=curlevelhead
                    curlevelhead=curlevelhead.next
                else:
                    break
    
            i+=1
            if i!=16:
                curlevelhead=prev.down
        

    def search(self, target: int) -> bool:
        self.searchpath(target)
        # if self.arr[15].next:
        #     print(\"Search\",self.arr[15].next.val)
        if self.arr[15].next and self.arr[15].next.val==target:
            return True
        return False
        
    def add(self, num: int) -> None:
        print(\"2\",num)
        self.searchpath(num)
        # print(arr)
        if self.arr[15].next and self.arr[15].next==num:
            a=1
        else:
            # head=self.levels[15]
            # print(\"printing added value before\")
            # while(head):
            #     print(head.val,end=\" \")
            #     head=head.next
            # print(\"\")
            i=1
            prev=None
            check=True
            while(i<=16):
                temp=self.arr[16-i].next
                # if temp:
                #     print(temp.val,\"10\")
                #     swapobj=temp.next
                #     temp.next=Node(num)
                #     temp.next.next=swapobj
                #     if prev:
                #         temp.next.down=prev
                #     prev=temp.next
                # else:
                self.arr[16-i].next=Node(num)
                self.arr[16-i].next.next=temp

                if prev:
                    self.arr[16-i].next.down=prev
                prev=self.arr[16-i].next
                check=self.coinflip()
                if check ==True:
                    # print(\"coinflip\",\"add\",num,i+1)
                    i+=1
                elif check == False:
                    head=self.levels[15]
                    # print(\"printing added value\")
                    # while(head):
                    #     print(head.val,end=\" \")
                    #     head=head.next
                    # print(\" \")
                    return 
            
                

    def erase(self, num: int) -> bool:
        
        print(\"3\",num)
        self.searchpath(num)
        i=1
        check=False
        while(i<=16):
           
            temp=self.arr[16-i].next
            if temp and temp.val==num:
                check=True
                self.arr[16-i].next=self.arr[16-i].next.next
            i+=1
        head=self.levels[15]
        # print(\"erasing value\")
        # while(head):
        #     print(head.val,end=\" \")
        #     head=head.next
        # print(\" \")
        return check
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
