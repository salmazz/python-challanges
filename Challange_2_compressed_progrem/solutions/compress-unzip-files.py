import PySimpleGUI as sg

from zip_creator import make_archive

label = sg.Text("Select files to compress:")

input1 = sg.Input()

files_browse = sg.FilesBrowse("Choose", key="files")

label_destination_folder = sg.Text("Select Destination Folder")

folder_browse = sg.FolderBrowse("Choose", key="folder")

input2 = sg.Input()

compress_button = sg.Button('Compress')
output_label = sg.Text(key= "output", text_color="green", background_color="white")

window = sg.Window('File Compressor', layout=[[label, input1, files_browse],
                                              [label_destination_folder,input2, folder_browse],
                                              [compress_button, output_label]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")

window.close()