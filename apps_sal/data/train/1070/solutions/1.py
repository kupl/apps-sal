# cook your dish here
class Animal:
    def __init__(self):
        start, end, starting_time = map(int, input().split())

        self.ending_time = starting_time + abs(start - end)
        self.velocity = 1 if end >= start else -1

        self.eaten_by = -1, 10 ** 10

        self.start = start
        self.end = end
        self.starting_time = starting_time

    def will_collide(self, z):
        if self.starting_time > z.ending_time or self.ending_time < z.starting_time:
            return False

        if self.velocity == z.velocity:
            if self.starting_time > z.starting_time:
                self, z = z, self
            if z.start == self.start + self.velocity * (z.starting_time - self.starting_time):
                return z.starting_time
            else:
                return False

        if self.velocity == -1:
            self, z = z, self

        t = (z.start - self.start + z.starting_time + self.starting_time) / 2

        return t if self.starting_time <= t <= self.ending_time and z.starting_time <= t <= z.ending_time else False


def main():
    for _ in range(int(input())):
        no_cats, no_rats = map(int, input().split())

        Cats = [Animal() for i in range(no_cats)]

        for i in range(no_rats):
            rat = Animal()
            for j in range(no_cats):
                time = rat.will_collide(Cats[j])
                if time:
                    # print(time)
                    if time < rat.eaten_by[1]:
                        rat.eaten_by = j + 1, time

            print(rat.eaten_by[0])


main()
