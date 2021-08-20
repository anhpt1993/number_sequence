# number sequence

def input_data():
    while True:
        try:
            num = int(input())
            if num >= 1:
                return num
                break
            else:
                print("Please input an integer greater than 1. Try again: ")
                print()
        except ValueError:
            print("Input value shall be an integer, not a decimal or string. Try again: ")
            print()

if __name__ == '__main__':
    print("Enter the row number: ")
    rows = input_data()
    print("Enter the column number: ")
    columns = input_data()
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            print("{:5d}".format(column * row), end= " ")
        print()