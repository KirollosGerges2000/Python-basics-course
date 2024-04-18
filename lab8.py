#lab8 "dictionaries lab8"
#scripted by: Eng/Kirollos Gerges


convert_month= {"jan":"january",
                "feb":"febrauary",
                "mar":"march"}
#print march
print(convert_month["jan"])

#print(convert_month["Kirollos"])

print(convert_month.get("feb"))

print(convert_month.get("Kirollos","2y 7aga"))

