def Reverse(x):
    "This function reverses the words in a sentance"

    #splits the user input after every word and adds to a list
    a = x.split()

    #reverses the list
    a.reverse()

    #defines what will be used to space out words when re joined
    a1 = " "

    #regoins words and spaces with a1 and prints to user
    print(a1.join(a))


#takes user input
i = input("Enter sentance to be reversed: ")

#calls Reverse function
o1 = Reverse(i)
