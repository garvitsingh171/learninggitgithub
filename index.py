import random
n=random.randint(1,21)

def asking():
    return int(input())

user_num = asking()
if user_num<1 or user_num>20:
    print("Invalid input")
    user_num = asking()
else:
    while user_num != n:    
        if user_num > n:
            print("Too high!")
            user_num = asking()
        elif user_num < n:
            print("Too low!")
            user_num = asking()
        elif user_num == n:
            print("You got it!")
            break

# import random
# n=random.randint(1,21)
# user_num = int(input())
# if user_num<1 or user_num>20:
#     print("Invalid input")
# while user_num!= n:
#     if user_num>n:
#         print("Too high!")
#         break
#     elif user_num<n:
#         print("Too low!")
#         break
#     elif user_num==n:
#         print("You got it!")
#         break        