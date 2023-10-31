

def main():
    password = 0
    while True:
        print("Menu") # This is the menu
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        selection = int(input("Please enter an option: "))

        if selection == 1:
            num = int(input("Please enter your password to encode: "))
            password = encode(num)  # This calls the encode function to encode the inputted password
            print("Your password has been encoded and stored!")
            print(password)

        elif selection == 2:
            pass

        elif selection == 3:
            break



def encode(num): # This function encodes the password
    result = 0
    i = 1
    while num>0:
        result += (((num%10)+3)%10)*(10**(i-1))
        i+=1
        num //= 10
    return result


if __name__ == '__main__': # This calls the main method
    main()