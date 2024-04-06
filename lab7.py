#lab7 "if condition  in python"
#scripted by: Eng/Kirollos Gerges

#process
is_hungry=False
wants_to_eat=False

if is_hungry and wants_to_eat:
    print("go to eat you are hungery or just to eat")

elif is_hungry and not wants_to_eat:
    print("eat so you can survive!!!!")

elif not is_hungry and not wants_to_eat:
    print("Don't eat you are not hungry")
else:
    print("don't eat")