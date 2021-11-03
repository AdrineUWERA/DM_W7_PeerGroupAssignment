# Question 5
def truth_value():
    x = list(map(int, input("\nEnter a list of integers of list x separated by a blank space : ").strip().split()))
    y = list(map(int, input("\nEnter a list of integers of list y separated by a blank space : ").strip().split()))

    y_divides_x = set()
    for value in x:
        for num in y:
            if value % num == 0:
                y_divides_x.add(value)

    if len(y_divides_x) == len(x):
        print("True")
    else:
        print("False")


truth_value()
