def Binary(i,l):
    "Binary search fucntion"

    #creating variable "f" and assigning it False value.
    f = False

    #creating value "b" for bottom and setting it to 0 because 0 is lowesnt number in list.
    b = 0

    #getting length of list and reduce by 1 to know full lenght of list.
    t = len(l) -1
    
    #while loop that compares bottom to make sure its less than or equal to top
    #and also when "f" is still not found.
    while b <= t and not f:

        #code to split up list into top and bottom to get the middle "m".
        m = (b+t)//2

        #if middle list is = to "i" then set value of "f" to true, this will end the loop.
        #and print output to user.
        if nl[m] == i:
            f = True
            print("True")

        #if middle of list is less than "i" then the "b" will be equal to middle +1
        elif l[m] < i:
            b = m + 1

        #finally if "i" is in bottom half of list then set middle -1
        else:
            t = m - 1

    #if item is or isnt found in list then return value of "f".
    #if its not found false will be returned as the value of "f" has not been changed.
    return f

    
#Ordered list
nl = [2,3,5,7,9,13]

#low and high inputs
low = int(input("Enter Low number: "))
high = int(input("Enter High number: "))

#calling function with inout from "high" and list "nl".
isf = Binary(high,nl)

#printing restult to user if number isnt in list
if isf is False:
    print("False")



