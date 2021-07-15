class FileMaster():
    def __init__(self, f) : self.path, self.ex = f.rsplit('/',1)
    extension=lambda self:self.ex.split('.')[1]
    filename=lambda self:self.ex.split('.')[0]
    dirpath=lambda self:self.path+'/'
