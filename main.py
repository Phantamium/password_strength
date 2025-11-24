import random

points = 0

def main():

    def check_strength(password):
        points = 0

        if len(password) >= 8:
            points += 2

        if any(c.isupper() for c in password):
            points += 2

        if any(c.islower() for c in password):
            points += 2

        if any(c.isdigit() for c in password):
            points += 2

        if any (c in "!@#$%&*" for c in password):
            points += 2


        if points <= 2:
            print("Very Weak")
        
        elif points <= 4:
            print("Weak")

        elif points <=6:
            print("Medium")

        elif points <=8:
            print("Strong")
        
        else:
            print("Very Strong")

    def generate_password():

        password = ''
        l=[]

        upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_char = "abcdefghijklmnopqrstuvwxyz"
        special_char = "!@#$%&*"
        numbers = "0123456789"

        upper = random.choices(upper_char, k = 2)
        lower = random.choices(lower_char, k = 2)
        special = random.choices(special_char, k = 2)
        num = random.choices(numbers, k = 2)

        l = upper + lower + special + num
        random.shuffle(l)
        for i in l:
            password += i

        print(password)

    while True:
        print("\n---------------------\n")
        print("1. to Checking the strength of your password")
        print("2. to generate a very strong password")
        print("3. to exit the program")
        print("Make a choice- (1 / 2 / 3) ")
        print("\n---------------------\n")

        choice = input("Make a choice (1/2/3): ")

        if choice == "1":
            password = input("Enter the password: ")
            check_strength(password)
        elif choice == "2":
            generate_password()
        elif choice == "3":
            print("Bye.")
            break
        else:
            print("Invalid choice.")  

main()
