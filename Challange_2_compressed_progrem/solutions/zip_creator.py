import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed_files")
    dest_path.mkdir(parents=True, exist_ok=True)  # Create the destination directory if it doesn't exist

    # Generate a specialized name for the zip file based on the names of the files
    base_name = "_".join(pathlib.Path(filepath).stem for filepath in filepaths)
    zip_filename = dest_path / f"{base_name}_archive.zip"

    with zipfile.ZipFile(zip_filename, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)