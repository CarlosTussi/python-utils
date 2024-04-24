"""
Funcion calculates if number provided is prime or not

Input: integer positive number
------

Output: True (if number is a prime) or False
------
"""
def is_prime(num: int) -> bool:
    if (num <= 1):
        return False
    for i in range(2,num-1):                 #Iterates intermediate numbers from 2...num-1
        if(num % i == 0):                    #Checks if num is divisible by any intermediate number
           return False
    return True



"""
Given a prime number, find_next_prime returns the next prime number

Input:
------
    prime: int
        A prime number

Output:
-------
    candidate: int
        The next prime number

"""

def next_prime(prime : int) -> int:

    found = False
    candidate = prime + 1
    while(not found):
        if(is_prime(candidate)):
            found = True
        else:
            candidate+=1

    return candidate



#Keep dividing by a prime facotr un
"""
2^2+3^1+7^1 represented as a dictionary 
{
2:2,
3:1,
7:1
}
"""
def prime_factorization(n : int) -> dict:
    current_prime = 2
    factors = {}
    while(n > 1): #Keep looping until the remainder is not 1
        while(n % current_prime == 0):       
            factors[current_prime] = factors.setdefault(current_prime, 0) + 1 #Will increment exisitng factor or create new factor entry in the dict
            n = n / current_prime       #Keep dividing with the same prime
        current_prime = next_prime(current_prime) #Check the next prime

    return factors

# 2*5
def number_of_divisors(dict_factors):
    cumulator = 1
    for key in dict_factors:
        cumulator *= (dict_factors[key]+1)
    
    return cumulator


if __name__ == "__main__":
    dict_factors = prime_factorization(16110)
    print(number_of_divisors(dict_factors))