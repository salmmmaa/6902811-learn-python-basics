def main():
    numbers = input("Enter a list of numbers separated by commas : ")
    numbers = numbers.split(",")
    print("List of numbers : ", numbers)
    total_sum = 0
    for number in numbers:
        total_sum += int(number)
    print("Sum of numbers : ", total_sum)
    average = total_sum / len(numbers)
    print("Average of numbers :", average)
    up_average_number = 0
    for number in numbers:
        if int(number) > average:
            up_average_number += 1
    print("Number of numbers greater than the average : ", up_average_number)
    even_numbers = 0
    i = 0
    while i < len(numbers):
        if int(numbers[i]) % 2 == 0:
            even_numbers += 1
        i += 1
    print("Number of even numbers :", even_numbers)
if __name__ == "__main__":
    main()
