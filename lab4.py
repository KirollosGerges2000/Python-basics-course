#lab4 "Lists in python"
#scripted by: Eng/Kirollos Gerges

friends=[1,"Kirollos",True,False,[1,"2y 7aga"]]
mechas_store=["programming","python"]

#print True
print(friends[2])

#print [1,"2y 7aga"]
print(friends[-1])

#error out of range
#print(friends[-6])

#print "Kirollos",True
print(friends[1:3])

#print "Kirollos",True,False,[1,"2y 7aga"]
print(friends[1:])

#print "change false"instead of false 
friends[3]="change false"
print(friends)

# print ["programming","python","Bobos"]
mechas_store.append("Bobos")
print(mechas_store)

#use function insert to control the index
mechas_store.insert(1,"power")
print(mechas_store)

#use remove function to remove an item , must have parameters
mechas_store.remove("power")
print(mechas_store)

#use pop function to delete last item
mechas_store.pop()
print(mechas_store)

