def isPrime(x):
    "This function checks to see if n is prime"

    #counts up from 2 (because 1 can't be a prime) up until the integer before n.
    for n1 in range(2,n):
        # using an if statement and modulo operator to see if there is a reaminder on the division of n and a number in the n1 list
        if (n % n1) == 0:
            print("Sorry that's not a prime.")
            break
    # if the above calculation fails then the number is prime and will be printed to the user.
    else:
        print(n," is a prime.")

    
#takes user input
i = input("Enter a number to check if its prime: ")

#converts user input to integer for caulcation
n = int(i)

#calls isPrime function
o1 = isPrime(n)
