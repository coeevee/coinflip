#this flips a coim 
import random
#imports the random module
print("This program flips a coin enter in the number of flips you want")
numflip=int(input())
#gets the number of flips
heads=0
tails=0
#delcares the variables
for (i) in range (numflip):
    headortail=random.randint(0,1)
    #makes a rancom number between 0 and 1
    if headortail==0:
        heads=heads+1
    if headortail==1:
       tails=tails+1
    if i==numflip-1:
        print("number of heads outcomes "+str(heads))
        print("number of tails outcomes "+str(tails))
        #prints the number of heads and tails
        print("aurthor:coeevee")
        print("github.com/coeevee/coinflip")
        #prints the aurthor and the github page