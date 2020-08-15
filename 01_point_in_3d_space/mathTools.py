def sqrt(x):
    """
    Sqrt from the Babylonian method for finding square roots.
    1. Guess any positive number x0. [Here I used S/2]
    2. Apply the formula x1 = (x0 + S / x0) / 2. The number x1 is a better approximation to sqrt(S).
    3. Apply the formula until the process converges. [Here I used 1x10^(-8)]
    """
    S = x
    x_old = S
    x_new = S / 2
    while abs(x_new-x_old) > 1e-8:
        x_old = x_new
        x_new = (x_old + S/x_old) / 2
    return x_new

def main():
    import numpy as np
    numpyAnswer = np.sqrt(15)
    myAnswer = sqrt(15)
    print("Square root of 15 from numpy is {}, from scratch is {}".format(numpyAnswer, myAnswer))
    print("Difference is {}".format((numpyAnswer - myAnswer)))

if __name__ == '__main__':
    main()
