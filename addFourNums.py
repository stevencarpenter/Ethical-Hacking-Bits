'''
Steven Carpenter
CSCI 4830 Ethical Hacking
HW1 Problem 9
MUST BE RUN USING PYTHON3
'''

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize socket
sock.connect(('hitchens.cs.colorado.edu', 1234)) #conect to hitchens port 1234
time.sleep(3) #wait for a few secconds
nums = sock.recv(1024) 


print (nums)
#grab each number and store as an int 
first = int.from_bytes(nums[:4], byteorder = "little")
second = int.from_bytes(nums[4:8], byteorder = "little")
third = int.from_bytes(nums[8:12], byteorder = "little")
fourth = int.from_bytes(nums[12:], byteorder = "little")



print (first)
print (second)
print (third)
print (fourth)

total = first + second + third + fourth #sum the nums
print (total)
total = total.to_bytes(4, byteorder = "little") #turn them back to bytes
print (total)
sock.send(total) #send the bytes sum to hitchens

answer = sock.recv(4096) #recieve the reply with user and pass

sock.close() 
print(answer) #Username: vortex1 Password: Gq#qu3bF3'
