'''
Steven Carpenter
CSCI 4830 Ethical Hacking
HW1 Problem 10
'''

import hashlib
import string

pairs = {} #dictionary to store 12 hex match and values that hash to match it {'string of 12 hex': [array of matching values that hash to 12 hex]}
n = 0 #iterator
while n < 10000000: 
    stringOfn = str.encode(str(n)) 
    hashOfn = hashlib.md5(stringOfn).hexdigest() #hash stringOfn into md5 hex
    concat = hashOfn[:6] + hashOfn[26:] #concatenate first and last 6 chars
    pairs.setdefault(concat, []).append(stringOfn) #if the 12 hex isnt a key, add it and append n to the value array, if it is in pairs then it will just append the n to values
    n += 1

for key, value in pairs.items():
    if len(value) > 1: #if more than one value hashes to have same 12 hex then it is a collision
        print ("The 12 hex match is: ", key, "\n")
        print ("The matching inputs are : ", value, "\n")
        print ("The saylor-6 hash collision is ", hashlib.md5(value[0]).hexdigest(), "\n") #print the collision by calling the hash on the first value that caused it
        break