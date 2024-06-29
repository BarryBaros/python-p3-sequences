#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0: #If the input length is less than or equal to 0, print an empty list and return immediately.
        print([])
        return
    
    #Initialize a list with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    #Use a loop to generate the remaining Fibonacci numbers
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    print(fibonacci_sequence[:length])
    
    #Example usage
if __name__ == "__main__":
     print_fibonacci(9)