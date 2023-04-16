from operations import add, sub, mult, div
from help_text import print_help

def main():
    while True:
        option = input()
        if option == "q":
            break
        if option == "help":
            print_help()
        else:
            numbers = input().split()

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