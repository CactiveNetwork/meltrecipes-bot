from os import listdir


def get_all_files(dir: str, extension: str | None = None) -> list[str]:
    """
    Get all files in directory with given extension
    dir: directory to find files from
    extension: extension to look for (optional)
    """

    files = listdir(dir)
    filesFiltered = []

    for filename in files:
        if extension is not None:
            if filename.endswith(extension):
                filesFiltered.append(filename)
        else:
            filesFiltered.append(filename)

    return filesFiltered
