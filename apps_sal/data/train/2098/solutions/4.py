
class Solver:
    def solve(self):
        self.num_voters, self.num_parties = (int(x) for x in input().split())

        self.votes_per_party = [[] for _ in range(self.num_parties)]

        for _ in range(self.num_voters):
            party, price = (int(x) for x in input().split())
            party -= 1

            self.votes_per_party[party].append(price)

        for party in range(self.num_parties):
            self.votes_per_party[party].sort()

        max_necessary_votes = self.num_voters//2 + 1
        cost = lambda min_votes : self.conversion_price_with_fixed_votes(min_votes)
        return self.ternary_search(cost, 0, max_necessary_votes + 2)

    def ternary_search(self, func, begin, end):
        while begin + 1 < end:
            mid = (begin + end - 1) // 2
            if func(mid) <= func(mid + 1):
                end = mid + 1
            else:
                begin = mid + 1
        return func(begin)

    def conversion_price_with_fixed_votes(self, num_votes):
        current_votes = len(self.votes_per_party[0])
        total_cost = 0

        for votes in self.votes_per_party[1:]:
            if len(votes) >= num_votes:
                num_bought_votes = len(votes) - num_votes + 1
                total_cost += sum(votes[:num_bought_votes])
                current_votes += num_bought_votes

        
        if current_votes >= num_votes:
            return total_cost
        num_votes_to_buy = num_votes - current_votes

        votes_left = []
        for party in range(1, self.num_parties):
            votes_left += self.votes_per_party[party][-(num_votes-1):]
        votes_left.sort()

        return total_cost + sum(votes_left[:num_votes_to_buy])


solver = Solver()
min_price = solver.solve()
print(min_price)


