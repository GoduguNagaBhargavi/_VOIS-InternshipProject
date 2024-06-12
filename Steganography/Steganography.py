import cv2
import os
import string

img = cv2.imread("_VOIS.jpg")

msg = input("Enter Secret Message: ")

password = input ("Enter a Passcode: ")

d = { }
c = { }

for i in range (255):
    d[chr(i)] = i
    c[i] = chr(i)
    
x = 0
y = 0
z = 0

#Encryption

for i in range (len (msg)):
    img [x,y,z] = d[msg[i]]
    x = x + 1
    y = y + 1
    z = (z + 1) % 3

cv2.imwrite("EncryptedImage.jpg", img)

os.startfile("EncryptedImage.jpg")


#Decryption

message =" "

x = 0
y = 0
z = 0


pas = input ("Enter Passcode for Decryption: ")

if (password == pas):
    
    for i in range (len (msg)):
        
        message = message + c[img[x,y,z]]
        x = x + 1
        y = y + 1
        z = (z + 1) % 3
    print("Decrypted Message = ", message)
        
else:
    
    print ("You are not Authenticated.")




    


