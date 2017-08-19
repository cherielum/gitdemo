# ## Largest Number
#
# Given an list of numbers, print the largest of the numbers.


def largestNum(a,b,c,d,e):
    listOfNum = [a, b, c, d, e]
    maxNum = max(listOfNum)
    print 'The largest number is: %s '% (maxNum)

a= int(raw_input("Give me one number: "))
b= int(raw_input("Second number: "))
c= int(raw_input("Third number: "))
d= int(raw_input("Next number: "))
e= int(raw_input("Last number: "))
largestNum(a,b,c,d,e)
