def print_fibonacci(length):
    """Print a Fibonacci sequence list of given length."""
    if length <= 0:
        print([])
        return

    if length == 1:
        print([0])
        return

    # Start sequence
    fib = [0, 1]

    # Generate remaining numbers
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])

    print(fib)
