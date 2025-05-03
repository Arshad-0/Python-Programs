import random as r
random_num=r.randint(1,100)
print(random_num)

user_input=int(input("Enter a number "))

if random_num >user_input:
     print("your guess is less than the actual number .")
elif random_num < user_input:
     print("your guess is greater than the actual code .")
else :
     print("congrats you guess the correct number ")
    
print("game over ")          