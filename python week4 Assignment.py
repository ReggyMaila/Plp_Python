
def modify_content(content):
    """
    Modify the content before writing to a new file.
    This example converts all text to uppercase.
    """
    return content.upper()

def main():
    input_filename = input("Enter the filename to read from: ")

    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        modified_content = modify_content(content)

        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

