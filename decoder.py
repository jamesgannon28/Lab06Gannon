

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
            output = decode(password)
            print(f"The decoded password is {output}, and the original password is {password}")

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

def decode(password): # This function decodes the password
    output = ''
    password = str(password)
    for i in range(len(password)):
        if password[i] == "0":
            output += '7'
        elif password[i] == "1":
            output += '8'
        elif password[i] == "2":
            output += '9'
        else:
            newnum = int(password[i])-3
            output += str(newnum)
    return output

if __name__ == '__main__': # This calls the main method
    main()

