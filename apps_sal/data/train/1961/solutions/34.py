class BrowserHistory:

    def __init__(self, homepage: str):
        '''
        Initializes the object with the homepage of the browser.
        :type homepage: str
        '''
        self.history = [homepage]
        self.forward_pages = []

    def visit(self, url):
        '''
        Visits url from the current page.
        It clears up all the future history.
        :type url: str
        :rtype: None
        '''
        self.history.append(url)
        self.forward_pages = []

    def back(self, steps):
        '''
        Move steps back in history.
        :type steps: int
        :rtype: str
        '''
        while steps > 0 and len(self.history) > 1:
            self.forward_pages.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    def forward(self, steps):
        '''
        Move steps future in history.
        :type steps: int
        :rtype: str
        '''
        while steps > 0 and self.forward_pages:
            self.history.append(self.forward_pages.pop())
            steps -= 1
        return self.history[-1]
