# Question 3
class Listoperations:
    def __init__(self):
        self.A = list(map(int, input("\nEnter a list of elements(integers) separated by a blank space : ").strip().split()))
        self.B = list(map(int, input("\nEnter a list of elements(integers) separated by a blank space : ").strip().split()))

    def list_subset(self):  # checks if B is a subset of A
        for elements in self.B:
            if elements in self.A:
                return "B is a subset of A"
            else:
                return "B is not a subset of A"

    def list_difference(self):  # Computes the difference between list A and B, A-B
        lst = []
        for elements in self.A:
            if elements not in self.B:
                lst.append(elements)
        return lst

    def cartesian_product(self): # Computes the product of the 2 lists.
        product_set = [[i, j] for i in self.A for j in self.B]
        return product_set


obj = Listoperations()
print(obj.list_subset())
print(obj.list_difference())
print(obj.cartesian_product())
