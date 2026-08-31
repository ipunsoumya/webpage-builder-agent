from pathlib import Path


def load_instructions_file(file_path: str) -> str:
    """
    Loads instructions from a given file path.
    Args:
        file_path (str): The path to the instructions file.
    Returns:
        str: The content of the instructions file.
    """
    try:
        # Attempt to open the file in read mode with UTF-8 encoding.
        return Path(file_path).read_text(encoding='utf-8')
        # If the file not found raise exception
    except FileNotFoundError:
        print(f"[WARNING] File {file_path} not found.]")
        raise FileNotFoundError(f"File {file_path} not found.")
    except Exception as e:
        print(f"[ERROR] Exception occurred while loading {file_path}: {e}")
        raise Exception(f"Exception occurred while loading {file_path}: {e}")

