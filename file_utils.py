import os
import glob

class FileManager:
    def __init__(self, folder_name):
        """
        Class for application .txt files management
        folder_name (str): folder in which single .txt file is to be stored
        """
        self.folder_name = folder_name

    def read_single_text_file(self):
        """
        Function reads text file from objects folder name, if it is the only text file in the folder
        """
        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(script_dir, self.folder_name)
        text_files = glob.glob(os.path.join(folder_path, "*.txt"))

        if len(text_files) == 0:
            raise FileNotFoundError(f"No .txt file found in folder: {folder_path}. Exactly one is required.")
        if len(text_files) > 1:
            raise ValueError(f"There is more than one .txt file in folder: {folder_path}. Exactly one is required.")

        with open(text_files[0], "r", encoding="utf-8") as file:
            return file.read().strip()

def save_file(filename, content):
    """.
    filename (str), content (str);.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(content)


