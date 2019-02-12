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


