# Question 4
class St1:
    def __init__(self):
        self.A = list(map(int, input("\nEnter elements(integers) of list A separated by a blank space : ").strip(
        ).split()))
        size = int(input("Enter number of sub lists to have in the whole list R: "))

        self.R = [[int(input("Enter each element in the sublists as x1, x2...xn --> [[x1,x2], [x3, x4]...] :"))
                   for _ in range(2)] for _ in range(size)]
        self.cproduct_A = [[x, y] for x in self.A for y in self.A]

    def is_relation(self):
        list_difference = [x for x in self.R if x not in self.cproduct_A]
        if len(list_difference) == 0:
            return "R is a subset of A X A\nR is a relation on A"
        else:
            return f"R is not a subset of A because the following elements is in R but not in A {list_difference}"

    def is_set(self):
        for elements in self.R:
            if self.R.count(elements) != 1:
                return "R is not a set"

        return "R is a set"

    def is_reflex(self):
        none_members = []
        for x in self.A:
            if [x, x] not in self.R:
                none_members.append(x)

        if len(none_members) == 0:
            return "R is reflexive"
        else:
            return f"R is not reflexive because of:{none_members}"

    def is_symmetric(self):
        none_symmetric = []
        for [x, y] in self.R:
            if [y, x] not in self.R:
                none_symmetric.append([x, y])

        if len(none_symmetric) == 0:
            return "R is symmetric"
        else:
            return f"R is not symmetric because of :{none_symmetric}"

    def is_transitive(self):
        none_members = []
        for [x, y] in self.R:
            for p in self.A:
                if [y, p] in self.R and [x, p] not in self.R:
                    none_members.append([x, y])
                    none_members.append([y, p])

        if len(none_members) == 0:
            return "R is transitive"
        else:
            return f"R is not transitive because of :{none_members}"


obj = St1()
ret = obj.is_set()
print(ret)
if ret == "R is a set":
    print(obj.is_relation())
print(obj.is_reflex())
print(obj.is_symmetric())
print(obj.is_transitive())
