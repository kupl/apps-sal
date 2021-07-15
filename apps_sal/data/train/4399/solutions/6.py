U = 1
F = 2
R = 3


def fold_cube(num_list):
    print(num_list)
    nums = set(num_list)
    faces = set()
    print(nums)
    try:
        face = Face(nums.pop(), nums, faces)
    except:
        return False
    faces.add(face)
#     print(face.val)
#     print(face.borders())
#     for face in faces:
#         print(face.val, face.z)
#     return sum(f.z for f in faces) == 0
    fs = set(f.z for f in faces)
    return fs == {1, 2, 3, -1, -2, -3}


class Face:
    def __init__(self, val, nums, faces, x=F, y=R, z=U):
#         print(val, nums)
        self.nums = nums
        self.val = val
        self.z = z
        self.x = x
        self.y = y

        for num in self.borders():
            self.nums.remove(num)
            z, x, y = self.fold(num)
#             print(z, x, y)
            faces.add(Face(num, self.nums, faces, x=x, y=y, z=z))

    def borders(self):
        borders = []
        ds = (self.val - 1) // 5
        ms = (self.val - 1) % 5
        for num in self.nums:
            dn = (num - 1) // 5
            mn = (num - 1) % 5
#             print(ds, ms, dn, mn)
            if ds - dn == 0 and abs(ms - mn) == 1 or ms - mn == 0 and abs(ds - dn) == 1:
                borders.append(num)
#             if abs(self.val - num) in [1, 5]:
#                 borders.append(num)
#         print(borders)
        return borders

    def fold(self, num):
        relation = self.val - num
        if relation == 5:
            z = self.x
            x = -self.z
            y = self.y
        elif relation == -5:
            z = -self.x
            x = self.z
            y = self.y
        elif relation == 1:
            z = -self.y
            x = self.x
            y = self.z
        elif relation == -1:
            z = self.y
            x = self.x
            y = -self.z
        return z, x, y

    def __hash__(self):
        return self.val

    def __eq__(self, other):
        return self.val == other.val

