\"\"\"
重写而不是pop
用一个size 记录，这样就不会重新visit 旧的forward history

\"\"\"
class BrowserHistory:

    def __init__(self, homepage: str):
        self.page_stack = []
        self.cur_idx = None
        self.visit(homepage)
        

    def visit(self, url: str) -> None:
        
        if self.cur_idx== None:
             self.cur_idx = 0  
            
        else:
            while len(self.page_stack) > self.cur_idx + 1:
                self.page_stack.pop()
            self.cur_idx += 1
             
        self.page_stack.append(url)
   #    print(self.page_stack)

    def back(self, steps: int) -> str:
        new_idx = max(0, self.cur_idx - steps)
      #  print(\"b\",self.cur_idx,new_idx,self.page_stack)

        self.cur_idx = new_idx
        return self.page_stack[self.cur_idx]
        

    def forward(self, steps: int) -> str:
        new_idx = min(len(self.page_stack)-1, self.cur_idx + steps)
        self.cur_idx = new_idx
        return self.page_stack[self.cur_idx]
        

 
