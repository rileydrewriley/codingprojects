import pathlib
import zipfile

def make_archive(filepaths, destination):
    dest_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["to_dos.txt", "Bonus program.py"], destination="Desktop")
