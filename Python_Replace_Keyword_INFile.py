import argparse
import os

def replace_keyword(file_name, keyword, replace_with, output_file_name):
  """Replaces a keyword in a file and writes the updated contents to another file.

  Args:
    file_name: The name of the file to search and replace the keyword in.
    keyword: The keyword to search for.
    replace_with: The string to replace the keyword with.
    output_file_name: The name of the file to write the updated contents to.
  """

  # Open the input file in read mode.
  with open(file_name, "r") as input_file:
    # Read the contents of the input file into a string.
    file_contents = input_file.read()

  # Replace the keyword in the file contents with the replacement string.
  updated_file_contents = file_contents.replace(keyword, "\n" + replace_with)

  # Open the output file in write mode.
  with open(output_file_name, "w") as output_file:
    # Write the updated file contents to the output file.
    output_file.write(updated_file_contents)

  # Close the input and output files.
  input_file.close()
  output_file.close()

# Parse the command line arguments.
parser = argparse.ArgumentParser(description="Replace a keyword in a file.")
parser.add_argument("file_name", help="The name of the file to search and replace the keyword in.")
parser.add_argument("keyword", help="The keyword to search for.")
parser.add_argument("replace_with", help="The string to replace the keyword with.")
parser.add_argument("output_file_name", help="The name of the file to write the updated contents to.")
args = parser.parse_args()

# Call the replace_keyword function to replace the keyword in the file and write the updated contents to the output file.
replace_keyword(args.file_name, args.keyword, args.replace_with, args.output_file_name)

# Print a success message to the user.
print("The keyword has been replaced successfully.")
