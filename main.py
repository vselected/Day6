# Exercise 1
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    elif a % 2 == 1 or b % 2 == 1:
        if a > b:
            return a
        else:
            return b

# Check
print("Check of Exercise 1")
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))


# Exercise 2
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    mylist = text.split()

    if mylist[0][0] == mylist[1][0]:
        return True
    else:
        return False

# Check
print("Check of Exercise 2")
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


# Exercise 3
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False

#Check
print("Check of Exercise 3")
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))


#Exercise 4
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short"

# Check
print("Check of Exercise 4")
print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    pass

# Check
master_yoda('I am home')
master_yoda('We are ready')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    pass

# Check
almost_there(104)
almost_there(150)
almost_there(209)




#
#