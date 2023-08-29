#                       #1
cubed_num = range(1,11)

for num in cubed_num:
    print(num**3)
        





#                       #2
num = 2
while num <= 100:
    for factor in range(2, num):
        if num % factor == 0:
            break    
    else:
        print(num)
    num = num + 1






#                        #3
age = int(input("How old are you? "))
if age <= 18:
    print("You're a kid!")
elif age <= 65:
    print("You're an adult!")
else:
    print("You're a senior!")

# or
age = int(input("How old are you? "))
if age <= 18:
    print("You're a kid!")
elif age >= 18 and age <= 65:
    print("You're an adult!")
else:
    print("You're a senior!")    

    