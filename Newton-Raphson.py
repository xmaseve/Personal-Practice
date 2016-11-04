'''
Use Newton-Raphson method to approximate square root
'''
def newton_raphson(k):
    epsilon = 0.01
    guess = k/2.0
    num = 0.0
    while abs(guess**2 - k) >= epsilon:
        num += 1
        guess = guess - (guess**2 - k)/(2*guess)
    print 'numGuesses =', num
    return guess
