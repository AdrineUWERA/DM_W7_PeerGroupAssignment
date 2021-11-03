# Question 1
def set_repr():
    list1 = list((input("\nEnter a list of elements separated by a blank space : ").strip().split()))
    if len(list1) == len(set(list1)):
        print("True")

    else:
        output_set = set(list1)
        print(f'False, the set should be {output_set}')


set_repr()
