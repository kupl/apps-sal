class BrowserHistory:
    \"\"\"
        Represents the browser history contents, and methods to visit
        new urls, as well as move backwards and forwards in the 
        history and return the urls at those positions.
    \"\"\"
    
    
    def __init__(self, homepage: str):
        \"\"\"The class is first initialized with
           a starting homepage url added initially
           to the history.
        \"\"\"
        
        # Validation
        min_len, max_len = 1, 20
        if len(homepage) < min_len or len(homepage) > max_len:
            return None
        
        self.current_index = 0
        self.history = [homepage]

        
    def visit(self, url: str) -> None:
        \"\"\"Visits a new url.
        
           Visits a new url, adds it to the history, increases
           the history index position, and if we are currently
           in the back-contents of the history, we remove all
           forward contents except this new visit url which will
           be most recent in the history.
        
           Args:
              url (str): The url to visit and add to history.
             
           Returns:
              None
        \"\"\"
        
        # Validation
        min_len, max_len = 1, 20
        if len(url) < min_len or len(url) > max_len:
            return None
        
        steps_until_final = len(self.history) - self.current_index - 1
        
        # If we have moved back in the history, we delete all forward history
        if steps_until_final > 0:
            old_history = self.history
            self.history = []
            for url_index in range(0, self.current_index + 1):
                self.history.append(old_history[url_index])
           
        # Visiting new url afterward
        self.current_index += 1
        self.history.append(url)


    def back(self, steps: int) -> str:
        \"\"\"Moves backwards in the history an arbitrary amount of steps.
           
           Moves backwards in the history an arbitrary amount of steps.
           If we can no longer move backwards in history, we stop at
           the beginning of the history.
        
           Args:
              steps (int): The number of steps to move backwards.
             
           Returns:
              resulting_url (str): The url that resides after moving
                                   backwards in the history.
        \"\"\"
        
        # Validation
        min_steps, max_steps = 1, 100
        if steps < min_steps or steps > max_steps:
            return None
        
        resulting_url = None
        
        if steps > self.current_index:
            # We are going to the beginning of the history
            self.current_index = 0
            resulting_url = self.history[self.current_index]
        else:
            # We are within the bounds of the history
            self.current_index -= steps
            resulting_url = self.history[self.current_index]
        
        return resulting_url
            

    def forward(self, steps: int) -> str:
        \"\"\"Moves forward in the history an arbitrary amount of steps.
        
           Moves forwards in the history an arbitrary amount of steps.
           If we can no longer move forwards in history, we stop at
           the end of the history.
        
           Args:
              steps (int): The number of steps to move forward.
             
           Returns:
              resulting_url (str): The url that resides after moving
                                   forward in the history.
        \"\"\"

        # Validation
        min_steps, max_steps = 1, 100
        if steps < min_steps or steps > max_steps:
            return None
        
        resulting_url = None
        
        steps_until_final = len(self.history) - self.current_index - 1
        print('steps until final: ', steps_until_final)
        if steps > steps_until_final:
            # We are going to the end of the history
            self.current_index = len(self.history) - 1
            resulting_url = self.history[self.current_index]
        else:
            # We are within the bounds of the history
            self.current_index += steps
            resulting_url = self.history[self.current_index]
            
        return resulting_url
            

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
