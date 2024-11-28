def read_and_write_file():
    """
    Reads a file provided by the user, modifies its content,
    and writes it to a new file, handling potential errors gracefully.
    """
    try:
        # Get input file name from user
        input_file = input("input.txt: ").strip()
        
        # Validate input file
        if not input_file:
            raise ValueError("Input file name cannot be empty.")
        
        # Read the content of the input file
        with open(input.txt, 'r') as file:
            content = file.read()
        
        # Modify the content (for this example, we'll convert to uppercase)
        modified_content = content.upper()
        
        # Get output file name from user
        output_file = input("answer.txt: ").strip()
        
        # Validate output file
        if not output_file:
            raise ValueError("Output file name cannot be empty.")
        
        # Write the modified content to the output file
        with open(answer.txt, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully read from '{input_file}', modified content, and wrote to '{answer.txt}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to access '{input.txt}' or '{answer.txt}'.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function
if __name__ == "__main__":
    read_and_write_file()

