def check_dates(records):
    correct = 0; recoverable = 0; uncertain = 0
    for rec in records:
        rec = DateRange(*rec)
        if rec.correct: correct += 1
        elif rec.recoverable: recoverable += 1
        elif rec.uncertain: uncertain += 1
    return [correct,recoverable,uncertain]

class Date:
    def __init__(self,date):
        self.date = [int(n) for n in date.split('-')]
        if 12<self.date[1]: self.date[2], self.date[1] = self.date[1:]; self.corrected = True
        else: self.corrected = False
        self.ambiguous = self.date[1]<13 and self.date[2]<13 and self.date[1]!=self.date[2]
    def swap(self):
        date = self.date[:]; date[2], date[1] = date[1:]
        return Date('-'.join([str(d) for d in date]))
    def __le__(self,other):
        if self.date[0]!=other.date[0]: return self.date[0]<other.date[0]
        if self.date[1]!=other.date[1]: return self.date[1]<other.date[1]
        return self.date[2]<=other.date[2]

class DateRange:
    def __init__(self,start,end):
        self.start = Date(start); self.end = Date(end)
        self.correct = None; self.recoverable = None; self.uncertain = None
        self.ambiguous = self.start.ambiguous or self.end.ambiguous
        if not self.ambiguous and self.start<=self.end:
            if self.start.corrected or self.end.corrected: self.recoverable = True
            else: self.correct = True
        else:
            self.start = [self.start]; self.end = [self.end]
            if self.start[0].ambiguous: self.start.append(self.start[0].swap())
            if self.end[0].ambiguous: self.end.append(self.end[0].swap())
            self.ranges = [(self.start[0],self.end[0])]
            if self.end[0].ambiguous: self.ranges.append((self.start[0],self.end[1]))
            if self.start[0].ambiguous:
                self.ranges.append((self.start[1],self.end[0]))
                if self.end[0].ambiguous: self.ranges.append((self.start[1],self.end[1]))
            self.ranges = [r for r in self.ranges if r[0]<=r[1]]
            if len(self.ranges)==1:
                if self.start[0]==self.ranges[0][0] and self.end[0]==self.ranges[0][1]: self.correct = True
                else: self.recoverable = True
            else: self.uncertain = True

