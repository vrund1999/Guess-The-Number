def main():
    print("Welcome to the number guessing game!")
    print("Enter a guess and you will be given hints if your guess is too high or too low.\n")
    print("The random number generated will be generated in between 0 and 50.")
    
    #Generate a random number first from 1 to 50
    random_Num = random.randrange(50)
    
    #Keep asking the user for their input and testing their input for validity and its value relative to the random number generated
    found = False
    while not found:
        user_input = input("Enter your guess: ")
        valid = False
        while not valid:
            try:
                int(user_input)
                valid = True
            except Exception as e:
                print("Try again, not an acceptable whole number.")
                user_input = input("Enter your guess: ")
        if user_input == str(random_Num):
            found = True
            print("\nYou got it!")
            print("The random number was:", random_Num)
        elif int(user_input) < random_Num:
            print("Your answer is too low!")
        else:
            print("Your answer is too high!")

if __name__ == "__main__":
    import random
    main()