#lab11 "preventing errors and reading files lab11"
#scripted by: Eng/Kirollos Gerges

#prevent user from run time error
#by using try and except
try:
    result=32/0
    value=int(input("Enter value:"))
    print(value)
except ZeroDivisionError as error:
    print(error)
except ValueError as value_error:
    print(value_error)
print("success")


#reading files
#open this file in read mode
FILE=open("FILE.txt","r")
#open this file in write mode
FILE=open("FILE.txt","w")
#open this file in append mode
FILE=open("FILE.txt","a")
#open this file in read,write mode
FILE=open("FILE.txt","r+")
#print true in read and false in write
print(FILE.readable())
#print Kirollos Gerges >>>>>>>Embedded C enginnering 
print(FILE.read())
#print Kirollos Gerges
print(FILE.readline())
#print Kirollos Gerges >>>>>>>Embedded C enginnering 
print(FILE.readlines())
#print Embedded C programming
print(FILE.readlines()[1])
FILE.close()




