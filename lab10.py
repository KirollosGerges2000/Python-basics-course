#lab10 "Exponent function and nested loops lab10"
#scripted by: Eng/Kirollos Gerges

#use exponent
#print 8
print(2**3)

#Nested loops [2D List]
no_list=[[1,2,3],[4,5,6],[7,8,9],[0]]

# print [[1,2,3],[4,5,6],[7,8,9],[0]]
print(no_list)

#print first row
print(no_list[0])

#print 7
print(no_list[2][0])

#use for in nested loop
for x in no_list:
    #print [1, 2, 3]
#   [4, 5, 6]
#[7, 8, 9]
#[0]

    print(x)

for ROW in no_list:
    for column in ROW:
        print(column)
