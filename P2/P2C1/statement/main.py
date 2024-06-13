def main():
    left_number = input("Enter an integer number : ")
    right_number = input("Enter an integer number : ")
    operation = input("Enter the desired operation ['+', '-', '*', or '/'] : ")
    result = 0
    if not left_number.isnumeric() or not right_number.isnumeric():
        print("Error: both numbers must be integers")
    else:
        left_number = int(left_number)
        right_number = int(right_number)
        match operation:
            case "+":
                result = left_number + right_number
            case "-":
                result = left_number - right_number
            case "*":
                result = left_number * right_number
            case "/":
                if right_number == 0:
                    print("Error: division by zero is not allowed.")
                else:
                    result = left_number / right_number
            case _:
                print("Error: the operation symbol must be '+', '-', '*', or '/'.")

        print(f"The result of the operation is: {result}")

if __name__ == "__main__":
    main()
