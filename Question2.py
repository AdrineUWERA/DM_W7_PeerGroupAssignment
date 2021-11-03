# Question 2
from itertools import product


class SetOperations:
    def __init__(self):
        self.A = set(map(str, input("\nEnter a list of elements for set A separated by a blank space : ").strip().split()))
        self.B = set(map(str, input("\nEnter a list of elements for set B separated by a blank space : ").strip().split()))

    def is_subset(self):  # checks if B is a subset of A
        if self.B.issubset(self.A):
            return f"{self.B.issubset(self.A)}. B is a subset of A"
        else:
            return f"{self.B.issubset(self.A)}. B is not a subset of A"

    def set_difference(self):   # evaluates set A - Set B
        return f"A-B = {set(self.A.difference(self.B))}"

    def cartesian_product(self):    # evaluates the cartesian product of A and B
        product_set = product(self.A, self.B)
        return f"A×B ={set(product_set)}"


obj = SetOperations()
print(obj.is_subset())
print(obj.set_difference())
print(obj.cartesian_product())
