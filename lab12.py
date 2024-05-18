#lab12 "writing files lab12"
#scripted by: Eng/Kirollos Gerges

#open this file in append mode
files=open("FILE.txt","a")

# Kirollos Gerges >>>>>>>Embedded C enginnering
#>>>>>>Good Enginner
files.write("\nGood enginner")

list_of_phrases=["\n Firist","\n Second"]
files.write(list_of_phrases);

files.close()