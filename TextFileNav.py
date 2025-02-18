def main():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Read the file and store lines in a list
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Start navigation loop
    while True:
        print(f"\nThe file has {len(lines)} lines.")
        try:
            line_number = int(input("Enter a line number (0 to quit): "))
            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1]}", end="")
            else:
                print("Invalid line number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
