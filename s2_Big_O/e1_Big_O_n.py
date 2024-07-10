def print_items(n):
    # print_items accepts one argument 'n'. It will print
    # a sequence of numbers from 0 up to, but not including, 'n'.
    
    for i in range(n):
        # A for loop is initiated with 'i' iterating over
        # the sequence of numbers produced by range(n).
        # For each iteration, 'i' takes the current number in
        # the sequence from 0 up to but not including 'n'.
        
        print(i)
        # Inside the loop, print(i) is called. This prints
        # the current value of 'i' to the console. This
        # action is performed 'n' times due to the for loop,
        # resulting in printing of numbers from 0 to 'n - 1'.