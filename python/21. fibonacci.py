n = int(input("Enter number of n terms: "))
if n <= 0:
    print("Fibonacci series for", n, "terms is not defined")
else:
    first = 0
    second = 1
    print("The first", n, "numbers in Fibonacci series are:")
    for i in range(n):
        print(first, end="" if i == n - 1 else ", ")
        fib = first + second
        first = second
        second = fib
