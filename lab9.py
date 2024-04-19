#lab9 "while condition and for loop lab9"
#scripted by: Eng/Kirollos Gerges

#while loop

i=1
while i<=10:
    print(i)
    i+=1
    if i==6:
        #jump to while loop again
        #so out 2,3,4,5,7,8,9,10
        continue
    else: 
          print("The condition isn't true ")
  

for letter in "code":
     print(letter)

names=["Ahmed","Mohamed"]
for name in names:
     print(name)

#using length in for loop
for x in range(len(names)):
     print(x)
    