"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 1
    while len(list) <= number_of_primes:
        for i in range (2,count):
            if count % i != 0:
                list.append(count)

        count +=1

    return list
