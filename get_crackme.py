import bs4
import requests
import re
import os
import zipfile
import tkinter as tk
import sys
import platform

def process(url):
    fileID = url.split('/')[-1]

    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    heading = soup.find('h3')
    folder_name = heading.text
    folder_name = re.sub("'", "", folder_name)
    folder_name = re.sub(" ", "_", folder_name)

    if platform.system() == "Windows":
        full_folder_name = os.environ['USERPROFILE'] + '\\Desktop\\Samples\\crackmes.one\\' + folder_name
        os.mkdir(full_folder_name)

        fileContent = requests.get('https://crackmes.one/static/crackme/' + fileID + '.zip').content
        fileName = full_folder_name + "\\" + fileID + '.zip'
        with open(fileName, 'wb') as file:
            file.write(fileContent)

        with zipfile.ZipFile(fileName) as zfile:
            zfile.extractall(full_folder_name, pwd=b'crackmes.one')
    
    if platform.system() == "Linux":
        full_folder_name = '/home/' + os.environ['USER'] + '/Desktop/Samples/crackmes.one/' + folder_name
        os.mkdir(full_folder_name)

        fileContent = requests.get('https://crackmes.one/static/crackme/' + fileID + '.zip').content
        fileName = full_folder_name + "/" + fileID + '.zip'
        with open(fileName, 'wb') as file:
            file.write(fileContent)

        with zipfile.ZipFile(fileName) as zfile:
            zfile.extractall(full_folder_name, pwd=b'crackmes.one')

    sys.exit()
    
def main():
    root = tk.Tk()

    text_box = tk.Text(root, height=10, width=50)
    text_box.pack()

    button = tk.Button(root, text="Submit", command=lambda: process(text_box.get("1.0", "end-1c")))
    button.pack()

    # root.after(10000, text_box.destroy())
    root.mainloop()

if __name__ == "__main__":
    main()