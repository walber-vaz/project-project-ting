import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """
    Processes a file and adds it to the given instance.

    Args:
        path_file (str): The path to the file to be processed.
        instance (Queue): The instance to which the file will be added.

    Returns:
        dict or None: A dictionary containing information about the
        processed file, or None if the file is already in the instance.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
    """
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),  # type: ignore
        "linhas_do_arquivo": file,
    }
    instance.enqueue(file_dict)
    sys.stdout.write(f"{file_dict}\n")
    return file_dict


def remove(instance):
    """
    Removes an element from the given instance.

    Args:
        instance (list): The instance from which the element will be removed.

    Returns:
        dict: The removed file.

    Raises:
        None.

    Examples:
        >>> instance = [
            {'nome_do_arquivo': 'file1'},
            {'nome_do_arquivo': 'file2'}]
        >>> remove(instance)
        Arquivo file1 removido com sucesso
        {'nome_do_arquivo': 'file1'}
    """
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return None

    file = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n"
    )
    return file


def file_metadata(instance, position):
    """
    Retrieves the metadata of a file in a given instance at the
    specified position.

    Parameters:
        instance (str): The instance to search the file in.
        position (int): The position of the file in the instance.

    Returns:
        None
    """
    if position < 0 or position >= len(instance):
        sys.stderr.write("Posição inválida\n")
        return None

    file = instance.search(position)
    sys.stdout.write(f"{file}\n")
    return
