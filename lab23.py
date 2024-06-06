#Lab 23 [*kargs,**kwargs]
#scripted by:
#Eng/Kirollos Gerges


# Program to add and display the sum of n number of integer
def add(*num):
    sum = 0;
    for n in num:
        sum = sum + n;
    print("Sum:", sum)

add(2,6)
add(3,4,5,6,7)
add(1,2,3,5,6,7,8)


# Print values of function Person along with its associated keywords
def Person(**kwargs):
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))    # OR print(f'{key} -> {value}')

Person(Name = 'Sean', Sex = 'Male', Age = 38, City = 'London', Mobile = 9375821987)