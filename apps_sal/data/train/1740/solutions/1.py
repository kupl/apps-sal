class Person:
    def __init__(self, name, my_family, gender='A'):
        self.name = name      # string
        self.children = []    # list of person objects
        self.parents = []     # list of person objects
        # A cluster represents a subset of a family partitioned by the
        # transitive closure of the relationship 'has a child in common with'
        self.cluster = {self, }
        self.gender = gender  # will be 'A' if unknown
        my_family.known_persons[name] = self


class family:
    def __init__(self):
        # Dictionary mapping names to person objects
        self.known_persons = {}

    # The letters M and F stand for 'known to be male' and 'known to be female'. The
    # letters A and B represent opposite genders within each cluster, but it is not
    # known which of the two letters represents male or female for that cluster.
    @staticmethod
    def __opposite_gender__(gender):
        return {'M': 'F', 'F': 'M', 'A': 'B', 'B': 'A'}[gender]

    # A common implementation of the mandatory methods 'male' and 'female'
    def __define_gender__(self, person, gender):
        if person in self.known_persons:
            if self.known_persons[person].gender in ('A', 'B'):
                # We are now able to fill in the correct gender not only for
                # this person, but for all the members of its cluster
                original_gender = self.known_persons[person].gender
                opposite_new_gender = family.__opposite_gender__(gender)
                for p in self.known_persons[person].cluster:
                    p.gender = gender if p.gender == original_gender else opposite_new_gender
            else:
                # Gender already known: check consistency
                return self.known_persons[person].gender == gender
        else:
            # First time we hear about this person; create them
            self.known_persons[person] = Person(person, gender=gender, my_family=self)
        return True

    def male(self, person):
        return self.__define_gender__(person, 'M')

    def female(self, person):
        return self.__define_gender__(person, 'F')

    def is_male(self, person):
        return person in self.known_persons and self.known_persons[person].gender == 'M'

    def is_female(self, person):
        return person in self.known_persons and self.known_persons[person].gender == 'F'

    # Auxiliary method to test for cycles in family trees
    def __is_ancestor_of__(self, p1, p2):
        if p1 == p2:
            return True
        elif len(p1.children) == 0:
            return False
        # Recursion: if one of my children is an ancestors of p2, then so am I
        for c in p1.children:
            if self.__is_ancestor_of__(c, p2):
                return True
        return False

    # Auxiliary method to join 2 existing clusters after a member of each of them
    # have acquired a common child, and to optionally adjust unknown genders in 1 of the clusters
    # based on the genders in the other cluster (which may be known or unknown)
    @staticmethod
    def __join_cluster__(old_cluster, new_cluster, source_gender, target_gender, modify_genders=True):
        for p in old_cluster:
            if modify_genders:
                if p.gender == target_gender:
                    p.gender = family.__opposite_gender__(source_gender)
                else:  # p.gender still unknown, but opposite of target_gender
                    p.gender = source_gender
            new_cluster.add(p)
            p.cluster = new_cluster

    # This method is the crux because despite its simple name, it has multiple functions:
    # - check/update parent-child relationships including cycles
    # - create 0, 1 or 2 new persons
    # - join existing clusters if necessary
    # We define different procedures depending on whether child and/or parent existed yet
    def set_parent_of(self, child, parent):
        # Eliminate a silly test case
        if child == parent:
            return False
        if child not in self.known_persons:
            # The child is new.
            p = self.known_persons[parent] if parent in self.known_persons else Person(parent, my_family=self)
            c = Person(child, my_family=self)
        else:
            # The child exists. Darn.
            c = self.known_persons[child]
            if parent not in self.known_persons:
                # New parent, existing child
                if len(c.parents) >= 2:
                    # Can't have 3 parents
                    return False
                p = Person(parent, my_family=self)
                if len(c.parents) == 1:
                    # Child already had a parent: put the new parent in the same cluster as the existing parent
                    family.__join_cluster__(p.cluster, c.parents[0].cluster, c.parents[0].gender, p.gender)
            else:
                # Both child and parent were known
                p = self.known_persons[parent]
                if c in p.children:
                    # Parent/child relationship was already known: do nothing
                    return True
                if len(c.parents) >= 2:
                    # p wasn't your parent yet and you can't have 3 parents
                    return False
                if self.__is_ancestor_of__(c, p):
                    # Can't have a cycle in the ol' family tree
                    return False
                if len(c.parents) == 1:
                    other_parent = c.parents[0]
                    # Child had 1 other parent: check gender compatibility between clusters;
                    # if necessary, join two clusters.
                    if other_parent.cluster == p.cluster \
                            or other_parent.gender in ('M', 'F') and p.gender in ('M', 'F'):
                        if other_parent.gender == p.gender:
                            # We already know that these 2 people have the same gender
                            # (perhaps even without knowing which gender it is)
                            # so they cannot become parents of the same child.
                            return False
                        elif other_parent.cluster != p.cluster:
                            # Consistent genders in different clusters:
                            # join the 2 clusters without modifying genders
                            family.__join_cluster__(p.cluster, other_parent.cluster,
                                                    other_parent.gender, p.gender,
                                                    modify_genders=False)
                    elif p.gender in ('A', 'B'):
                        # join 2 clusters, at most 1 of which has known genders
                        family.__join_cluster__(p.cluster, other_parent.cluster, other_parent.gender, p.gender)
                    elif other_parent.gender in ('A', 'B'):
                        # Join 2 clusters, exactly 1 of which had known genders: transfer that knowledge
                        family.__join_cluster__(other_parent.cluster, p.cluster, p.gender, other_parent.gender)
                    else:
                        print("add_parent: unknown gender combination")
                        return False
        # Finally do what we came here for
        c.parents.append(p)
        p.children.append(c)
        return True

    def get_parents_of(self, person):
        return sorted([p.name for p in self.known_persons[person].parents]) if person in self.known_persons else []

    def get_children_of(self, person):
        return sorted([c.name for c in self.known_persons[person].children]) if person in self.known_persons else []

