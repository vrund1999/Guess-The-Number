def main():
    #Generate a random number first from 1 to 50
    random_Num = random.randrange(50)
    print(random_Num)

    found = False
    while not found:
        user_input = input("Enter your guess: ")
        if user_input == str(random_Num):
            found = True
            print("You got it!")
        elif int(user_input) < random_Num:
            print("Your answer is too low!")
        else:
            print("Your answer is too high!")

if __name__ == "__main__":
    import random
    main()