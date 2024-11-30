def modify_file_content(content):
    """
    Modify the content read from a file.
    Example modification: Convert text to uppercase.
    """
    return content.upper()  # Modify as needed (e.g., add lines, replace words, etc.)

def main():
    try:
        # Prompt the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open and read the input file
        with open(input_filename, "r") as infile:
            original_content = infile.read()

        # Modify the file content
        modified_content = modify_file_content(original_content)

        # Prompt the user for the output filename
        output_filename = input("Enter the name of the file to write the modified content to: ")

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File has been modified and saved to {output_filename} 🎉")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
