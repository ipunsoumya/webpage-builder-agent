import datetime
from pathlib import Path


def write_to_file(content: str) -> dict:
    """
    Writes the given content to a file named output/<timestamp>_generated_page.html under the /output/ directory.
    Args:
        content (str): The content to be written to the file.
    Returns:
        dict: A dictionary containing the status and filename of the written file.
    """
    timestamp = datetime.datetime.now().strftime("%m%d_%I%M%S")
    filename = f"output/{timestamp}_generated_page.html"
    Path("output").mkdir(exist_ok=True)
    Path(filename).write_text(content, encoding="utf-8")
    return {
        "status": "Success",
        "filename": filename
    }