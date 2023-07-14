import os
import sys


def txt_importer(path_file):
    """
    Reads a text file from the specified path and returns its contents
    as a list of lines.

    Parameters:
    - path_file (str): The path to the text file.

    Returns:
    - list of str: The contents of the text file as a list of lines.

    Raises:
    - TypeError: If the provided path_file is not a string.
    - ValueError: If the provided path_file does not end with '.txt'.
    - FileNotFoundError: If the file at the provided path_file does not exist.
    """
    if not path_file.endswith('.txt'):
        return sys.stderr.write("Formato inválido\n")

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    with open(path_file, 'r') as file:
        return file.read().split('\n')
