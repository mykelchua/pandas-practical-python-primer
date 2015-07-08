"""
This is my First Script on Python using CLI
"""

import argparse
import subprocess



def process_user_input():
    """
    Process Input from the Command Line and return the results.

    Returns:
        A argparse.Namespace object containing the results of
        parsing the command line input.
    """
    argument_parser = argparse.ArgumentParser(
        description="This Program will copy Files.",
        epilog="This Program copied Files."
    )

    argument_parser.add_argument(dest='filenames', metavar='filename',
                                 nargs='+', help="All the files to Copy.")

    argument_parser.add_argument('-d', '--destination', dest='destination',
                                 required=True,help='Location to copy files to.')

    argument_parser.add_argument('-n', '--newnames', dest='new_filenames',
                                 metavar='new_filename', nargs='+',
                                 help="New filenames for copied files.")

    return argument_parser.parse_args()

def copy_files(files, destination, new_filenames):
    """
    Copy files to a destination.

    Args:
        files (list): The files to be copied
        destination (str): Location to copy the files
    """

    for filename in files:
        if new_filenames is not None:
            try:
                file_destination = "{}/{}".format(
                    destination, new_filenames[files.index(filename)])
            except IndexError:
                print(
                      "No matching new name found for file : {}".format(filename))
                continue
        else:
            file_destination = destination

        operation_result = subprocess.check_output(
            args=['cp', '-vp', filename, file_destination],
            stderr=subprocess.STDOUT)
        print(operation_result.decode().strip('\n'))


if __name__ == "__main__":
    parsed_arguments = process_user_input()
    copy_files(parsed_arguments.filenames, parsed_arguments.destination,
               parsed_arguments.new_filenames)





