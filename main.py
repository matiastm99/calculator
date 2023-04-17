from operations import add, sub, mult, div
from help_text import print_help

def main():
    print("Type h or help to see available options.")
    print("Press q to quit.\n")

    while True:
        option = input("Enter an operation: ")
        if option == "q":
            break
        
        if (option == "h") or (option == "help"):
            print_help()
        else:
            numbers = input("Enter some numbers: ").split()

            if option == "add":
                print(add(numbers))
        
            if option == "sub":
                print(sub(numbers))

            if option == "mult":
                print(mult(numbers))
        
            if option == "div":
                print(div(numbers))

if __name__ == "__main__":
    main()
