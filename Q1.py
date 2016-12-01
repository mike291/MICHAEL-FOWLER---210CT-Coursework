import random

def ArrayShuff():
    "This function randomly shuffles an array of integers"
    
    #creates an array with integers 1,4,12,27,96
    a1 = [1,4,12,27,96]

    #this second array is the array that will be shuffled.
    cord1 = [0,1,2,3,4]

    #random.shuffle is used to reorder the placement of the second array of 0-4.
    random.shuffle(cord1)

    #this is where the reordered list "cord1" is applied to the original "a1" list
    a1 = [a1[i] for i in cord1]

    print(a1)

#Calls the function
o1 = ArrayShuff()

