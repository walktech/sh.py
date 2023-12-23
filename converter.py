import os

def convert_to_executable(input_file, output_extension):
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Generate the output filename by replacing the current extension
    output_file = os.path.splitext(input_file)[0] + output_extension

    try:
        # Read the content of the Python script
        with open(input_file, 'r') as file:
            script_content = file.read()

        # Write the content along with the shebang line to a new file
        with open(output_file, 'w') as file:
            file.write(f"#!/usr/bin/env python\n{script_content}")

        # Set execute permissions (Unix-based systems)
        os.chmod(output_file, 0o755)

        print(f"Conversion successful! Executable file created: {output_file}")
    except Exception as e:
        print(f"Error occurred during conversion: {e}")

