def read_and_write_file():
    """
    Reads a file provided by the user, modifies its content,
    and writes it to a new file, handling potential errors gracefully.
    """
    try:
        # Ask the user for the input filename
        input_filename = input("input.txt): ")
        
        # Attempt to open and read the file
        with open(input.txt, "r") as infile:  # Corrected variable name
            content = infile.readlines()  # Read all lines from the file
            
        # Modify the content (e.g., convert text to uppercase)
        modified_content = [line.upper() for line in content]
        
        # Ask the user for the output filename
        output_filename = input("answer.txt): ")
        
        # Write the modified content to a new file
        with open(answer.txt, "w") as outfile:  # Corrected variable name
            outfile.writelines(modified_content)
        
        print(f"Modified content successfully written to {answer.txt}. 🎉")
    
    except FileNotFoundError:
        print("Error: The file you specified does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read/write the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
