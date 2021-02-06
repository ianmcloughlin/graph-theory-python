"""Verifiying the Collatz conjecture."""

# Ian McLoughlin

def f(n):
    # If n is even.
    if n % 2 == 0:
        return n // 2
    # If n is odd.
    elif n % 2 == 1:
        return (3 * n) + 1
    # If n is 0, but it shouldn't be.
    else:
        return None

def collatz(n):
    """Check the Collatz conjecture is True for n."""
    # Make sure n is a positive integer.
    if type(n) is not int or n < 1:
        return None
    # Keep track of the numbers generated so far.
    so_far = []
    # Loop until n is 1.
    while n != 1:
        # If we see a number greater than 1 twice, Collatz is false.
        if n in so_far:
            return False
        # Save n to list.
        so_far.append(n)
        # Generate next n.
        n = f(n)
    # Add 1 to the end.
    so_far.append(n)
    # Return the sequence in the list.
    return so_far

print(collatz(10435634634600032434))
