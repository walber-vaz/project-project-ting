def exists_word(word, instance):
    """
    Generate a list of dictionaries representing occurrences of a given word
    in a list of files.

    Args:
        word (str): The word to search for.
        instance (Instance): An instance object containing a list of files.

    Returns:
        list: A list of dictionaries representing the occurrences of the word
        in the files. Each dictionary contains the following keys:
            - palavra (str): The word.
            - arquivo (str): The name of the file.
            - ocorrencias (list): A list of dictionaries representing the
            occurrences of the word in the file. Each dictionary contains
            the following keys:
                - linha (int): The line number where the word occurs.
    """
    archives = [
        {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": line}
                for line, line_content in enumerate(
                    file["linhas_do_arquivo"], start=1
                )
                if word.lower() in line_content.lower()
            ],
        }
        for file in instance._list
        if any(
            word.lower() in line_content.lower()
            for line_content in file["linhas_do_arquivo"]
        )
    ]

    return archives


def search_by_word(word, instance):
    """
    Search for occurrences of a given word in a list of files.

    Parameters:
        word (str): The word to search for.
        instance (Instance): An instance object containing a list of file data.

    Returns:
        list: A list of dictionaries, each containing information about a file
        where the word was found. Each dictionary has the following keys:
            - palavra (str): The searched word.
            - arquivo (str): The name of the file.
            - ocorrencias (list): A list of dictionaries, each containing the
            line number and content where the word was found. Each dictionary
              has the following keys:
                - linha (int): The line number.
                - conteudo (str): The line content.
    """
    results = []

    for file_data in instance._list:
        file_name = file_data["nome_do_arquivo"]
        occurrences = []

        for line_number, line_content in enumerate(
            file_data["linhas_do_arquivo"], start=1
        ):
            if word.lower() in line_content.lower():
                occurrence = {"linha": line_number, "conteudo": line_content}
                occurrences.append(occurrence)

        if occurrences:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences,
            }
            results.append(result)

    return results
