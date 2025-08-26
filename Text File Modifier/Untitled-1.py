def modify_content(content):
    """
    Modify the content of the file.
    This version numbers each line in the file.
    Example:
    1: First line
    2: Second line
    """
    lines = content.splitlines()
    numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
    return "\n".join(numbered_lines)


def main():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r", encoding="utf-8") as infile:
            content = infile.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create new filename
        new_filename = "modified_" + filename

        # Write the modified content to new file
        with open(new_filename, "w", encoding="utf-8") as outfile:
            outfile.write(modified_content)

        print(f"Modified file saved as {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read the file.")


if __name__ == "__main__":
    main()
