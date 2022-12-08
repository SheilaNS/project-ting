from ting_file_management.queue import Queue


def get_line(index, content, is_content):
    if is_content:
        return {"linha": index, "conteudo": content}
    return {"linha": index}


def exists_word(word, instance: Queue, is_content=False):
    """Aqui irá sua implementação"""
    result = []
    for info in range(len(instance)):
        data = instance.search(info)
        occurrences = [
            get_line(index + 1, content, is_content)
            for index, content in enumerate(data["linhas_do_arquivo"])
            if word.lower() in content.lower()
        ]
        result_item = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": occurrences,
        }
        if occurrences:
            result.append(result_item)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
