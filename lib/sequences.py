#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    fibonacci_sequence = []  # List to store Fibonacci numbers
    
    # Generate Fibonacci sequence up to the specified length
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b  # Update to the next Fibonacci numbers
    
    print(fibonacci_sequence)

# Example usage:
print_fibonacci(9)
