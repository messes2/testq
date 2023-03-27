
#write a function that takes two arguments, the first argument is a string (guranteed to be a string), the second argument is a number,
#find all of the number in the string, increment those numbers by the second argument, and then return a string with all the numerical values
#groupings of character or number, list never empty

#outline of strategy
# 1. RegEx for decimals and not decimals (check what asciis go where)
# 2. List comprehension to grab the correct format from the Regex text
# 3. Determine if first substring is a number, if so, have index start at 0
# 4. index over the strings in the list and add the number offset
# 5. use "".join(list) method to return the final values as a string

import random, string
import re

def incrementstringvalues(string, number):
    # Find all patterns in the string
    pattern = r'((\d+)|(\D+))'
    matchlist = re.findall(pattern, string)

    # List comprehension to format the regex tuples
    returnlist = [match[0] if match[0] else ''.join(match[1:]) for match in matchlist]

    # Determine starting index for number count
    eo = 1  # Index starts at 1 because each string is either all letters/symbols or all numbers
    if (returnlist != []) and (returnlist[0][0].isdigit()): # Check if digit or null string
        eo = 0

    # Update numbers with offset
    for i in range(eo, len(returnlist), 2): # Start at first number count
        returnlist[i] = str(int(returnlist[i]) + number)

    # Return list as string
    return "".join(returnlist)


#Given a length, return a string of random characters, this is good for validating

def testvalues(length):#function to generate random test values
    random_char = string.ascii_letters + string.digits +string.punctuation #combines three lists to be all characters
    randomstring= ''.join([random.choice(random_char) for i in range(length)])#joins the string
    print("The random string used was",randomstring)#prints so that you can check it
    return randomstring#return random string

print(incrementstringvalues("64force500@@@0point9999", 15))
print(incrementstringvalues("force500@@@0point9999", 15))
print(incrementstringvalues("", 15))
print(incrementstringvalues("aaaaaaaaaaaaaaaaaaaaaaaaaaa", 15))
print(incrementstringvalues("0", 15))
testnum=testvalues(50)#basic cryptography check
print("the encrypted string is   ", incrementstringvalues(testnum,15))
print("the decrypted string is   ", incrementstringvalues(incrementstringvalues(testnum,15),-15))#basic cryptography check



    