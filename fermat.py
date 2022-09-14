import random
from math import floor


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


# efficiently mods large numbers
# Time complexity O(n^3) - detailed below
# Space complexity O(n^2) - because of recursive nature
def mod_exp(x, y, N):  # x is the base case, y is the exp and N is our Mod number
    if y == 0:  # then we have reached the base case and anything to 0 is 1
        return 1
    z = mod_exp(x, floor(y / 2), N)  # allows us to "keep track" and recurse out once we have found if it is zero or not

    if y % 2 == 0:
        return (z ** 2) % N  # O(n^2)
    return (x * z ** 2) % N  # O(n^2)
# repeated n times for O(n^3)


# probability of fermat being right
def fprobability(k):
    # You will need to implement this function and change the return value.   
    return (1 - (1 / (2 ** k)))


# probability of millar-rabin being right
def mprobability(k):
    # You will need to implement this function and change the return value.   
    return (1 - (1 / (4 ** k)))


# for k iterations, chooses a random a base, and calles mod_exp to make sure that
# it never finds anything besides 1, in which case it is probably prime
# Time complexity - O(kn^3) - k iterations of mod_exp which is O(n^3)
# Space complexity - O(n^2) - as much as mod_exp
def fermat(N, k):
    for i in range(1, k):   #O(k) iterations,
        a = random.randint(1, (N - 1))   #O(log(n)) for rand int
        if not mod_exp(a, (N - 1), N) == 1: #O(n^3) for mod_exp
            return 'composite'
    return 'prime'


# tests numbers that have passed the fermat test by taking repeated square roots
# to further weed out carmichael numbers. If the mod_exp of this square rooted
# number does not equal one, we have found a composite
# if the number's exponent reaches an odd power after running through
# square root tests, or returns a value of (N-1) then we have found a prime
# Time complexity - O(k^2n^5log(y))
# Space complexity - O(n^2) - no more than fermat or mod_exp at one time
def miller_rabin(N, k):
    if fermat(N, k) == 'prime':  #O(kn^3)
        for i in range(1, k):  #O(k)
            a = random.randint(1, (N - 1)) #O(logn)
            y = N - 1
            while y != 0: #O(log(y))
                b = mod_exp(a, y, N) #O(n^2)
                if y % 2 == 1 or b == (  #O(n^2) for very bad mod cases
                        N - 1):  # if you get an odd exponent or hit N-1 then the Miller-Rabin test stops and returns "prime"
                    return 'prime'
                if not b == 1:
                    return 'composite'
                else:
                    y = y / 2
    return 'composite'
