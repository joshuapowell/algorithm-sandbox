"""
Binary Search Algorithm.


Questions:

    - How is linear search represented using Big O notation?
    - How is binary search represented using Big O notation?
    - How do I calculate the maximum worse case, given a maximum value?


Describe:

    A guessing game, with a low number and high number, the computer sets
    a random number from the lowest to highest number. To win the game you
    must guess what the random number is chosen by the computer.

    How do you find the number?

       Assumptions: Minimum and maximum are integers.

    1. Set a minimum and maximum variable.
    2. If number entered is equal to random number, you win the game.
    3. If the number guessed is less than the random number, set the minimum
       value to one greater than the number guessed.
    4. If the number guessed is greater than the random number, set the
       maximum value to one lower than the number guessed.
    5. Return to step 2 and repeat until the random number is matched.

"""


import math


def all_prime():
    """Generate a list of all prime numbers between 0 and 100."""

    tmp_data = range(0, 97)

    for index, value in enumerate(tmp_data):
        if value % 2 == 0:
            tmp_data.pop(index)
    
    return tmp_data

primes = all_prime()

static_primes =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def example_1(data, targetValue):

    min_ = 0
    max_ = len(data)-1
    guess = None
    guessCounter = 1

    while max_ >= min_:

        guess = int(math.floor((min_+max_)/2))
        print "Current guess", guess
    
        if data[guess] == targetValue:
            print "It took %s guess to find the target value" % (guessCounter)
            return guess
        elif data[guess] < targetValue:
            min_ = guess + 1
        elif data[guess] > targetValue:
            max_ = guess - 1

        guessCounter = guessCounter + 1

test = example_1(static_primes, 73)

print "Data", primes
print "Found prime at index", test
