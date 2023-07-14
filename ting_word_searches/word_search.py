def exists_word(word, instance):
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
