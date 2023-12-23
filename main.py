import argparse
from converter import convert_to_executable

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Python script to an executable.")
    parser.add_argument("filename", help="Name of the Python script file")
    parser.add_argument("-e", "--extension", default=".sh", help="Output executable file extension (default: .sh)")
    args = parser.parse_args()

    convert_to_executable(args.filename, args.extension)

