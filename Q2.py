#While loop that runs program again after completion of main code.
while True:
    try:
        x = input("Input number you would like to know the Factorial of : ")
        x1 = int(x)
    except:
        continue

    #ensures user enters a positive integer
    if x1 < 0:
        print("Sorry you must enter a positive integer")
        
    #code to calculate the factorial number from user input
    elif x1 >= 0:
        c = 1
        while x1 >= 1:
            c =  c * x1
            x1 = x1 -1
        print(c)

    #code to calculate the number of trailing 0's of the factorial
    #Sets a value of 0 to variable named "trail"
    trail = 0
    #begins a while loop so that if the factorial has multiple trailing 0's then they can all be counted
    while True:
        #if statemtn to check to see if there is another 0 at end of factorial, does this by dividing factiorial by factor of 10 and returning the remainder.
        if c % 10 == 0:
            #if there is another 0 at end of factorial then 1 is added onto the "trail" variable previsoly set
            trail += 1
            c = c / 10
        #While loop breaks when there is no 0 at end of factorial          
        else:
            break

    print("number of trailing 0s is: ", trail)


    

