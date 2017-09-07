# This if for anything related to Math computations

def check_if_prime_number(num):
    """Print if a number is a prime number or not and display its factors"""
    if (num < 2):
        print(num, "is not a prime number.")

    # To make computation more efficient, you can split the range by half
    for x in range(2,num):
        if (num%x == 0):
            print(num, "is not a prime number.")
            print(num, "has a factor of", x, "and", int(num/x) )
            break
    else:
        print(num, "is a prime number.")

    return
