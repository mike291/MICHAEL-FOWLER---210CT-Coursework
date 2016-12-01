def RemVowels(x):
    "This function removes vowels from a string"

    #Takes user string and replaces a,e,i,o,u with nothing
    s1 = s.replace("a", "")
    s2 = s1.replace("e", "")
    s3 = s2.replace("i", "")
    s4 = s3.replace("o", "")
    s5 = s4.replace("u", "")

    print(s5)

#takes user input
s = input("Enter string: ")

#calls RemVowels function
o1 = RemVowels(s)
