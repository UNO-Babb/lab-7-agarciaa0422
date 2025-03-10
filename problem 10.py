#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime2

#def main():  
    #limit_num = 2000000
    #prime = summation_prime(limit_num)
    #print("The sum of the primes below " + str(lim) + " is: " + str(summation_prime))

#tried something different on this but wasnt working out, as writing the code on number tests then just put the def_main to see if works.
 
def summation_prime(lim):
    total_summation = 0
    for num in range(2, lim):
        if isPrime2(num):
            total_summation = total_summation + num
    return total_summation

def main():  
    lim = 2000000
    prime = summation_prime(lim)
    print("The sum of the primes below " + str(lim) + " is: " + str(prime))

#cant figure this out

if __name__ == '__main__':
    main()