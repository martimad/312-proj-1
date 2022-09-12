import random
from math import floor


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


# efficiently mods large numbers
#
def mod_exp(x, y, N): #x is the base case, y is the exp and N is our Mod number
    if y == 0:  #then we have reached the base case and anything to 0 is 1
        return 1
    z = mod_exp(x, floor(y/2), N) #allows us to "keep track" and recurse out once we have found if it is zero or not

    if y % 2 == 0:
        return (z**2) % N #O(n^2)
    return (x * z**2) % N #O(n^2)


#probability of fermat being right
def fprobability(k):
    # You will need to implement this function and change the return value.   
    return (1-(1/(2**k)))


#probability of millar-rabin being right
def mprobability(k):
    # You will need to implement this function and change the return value.   
    return (1-(1/(4**k)))


#
#O()
def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most
    # likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    for i in range(1,k):
        a = random.randint(1, (N-1))
        if not mod_exp(a, (N-1), N) == 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for 'a', you will most likely want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    if fermat(N, k) == 'prime':
        for i in range(1, k):
            a = random.randint(1, (N-1))
            y = N - 1
            while y != 0:
                b = mod_exp(a, y, N)
                if y % 2 == 1 or b == (N-1):   #if you get an odd exponent or hit N-1 then the Miller-Rabin test stops and returns "prime"
                    return 'prime'
                if not b == 1:
                    return 'composite'
                else:
                    y = y/2

