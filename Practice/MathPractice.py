# This if for anything related to Math computations

def check_if_prime_number(num):
    """Print if a number is a prime number or not and display its factors"""
    status = False
    if (num < 2):
        print(num, "is not a prime number.")

    # To make computation more efficient, you can split the range by half
    else:
        for x in range(2,num):
            if (num%x == 0):
                print(num, "is not a prime number.")
                print(num, "has a factor of", x, "and", int(num/x), "." )
                break
        else:
            print(num, "is a prime number.")
            status = True

    return status

def display_fibonacci(lastNum):
    """Display the Fibonacci sequence up until the input number"""
    a = 0
    b = 1
    print("Fibonacci Sequence: ")
    while(b < lastNum):
        print(b, end=" ")
        a, b = b, a+b
    return

if __name__ == "__main__":
    check_if_prime_number(29)
    check_if_prime_number(30)
    display_fibonacci(2000)
