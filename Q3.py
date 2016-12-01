def PerfSquare(x):
    "This function will find the highest perfect square of an integer"

    #square roots the users input
    a = x ** (0.5)
    
    #converts square root to integer
    a1 = int(a)
    print(a1)

#takes user input
i = input("Enter inteeger to find highest perfect square which is less than or equal to it: ")

#converts user input to integer for function
i1 = int(i)

#calls PerfSquare Fucntion with value from user
o1 = PerfSquare(i1)

