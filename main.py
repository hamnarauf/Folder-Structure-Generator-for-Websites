import os

def createFolder(folder):
    ''' Creates a folder at a specific path'''
    completePath = os.path.join(path, folder)
    try:
        os.makedirs(completePath)
        print(completePath + " created successfully.")
    except:
        print(completePath + " already exists.")


def createFile(file, folder=""):
    ''' Creates a file at a specific path'''
    completePath = os.path.join(path, folder, file)
    try:
        open(completePath, "x")
        print(completePath + " created successfully")
    except:
        print(completePath + " already exists")


def writeToFile(filePath, text):
    '''Writes text to a file'''
    try:
        file = open(filePath, "w")
        file.write(text)

    except:
        print("Error occured while writing to the file")
    finally:
        file.close()


# Boiler plate for html
html_boilerPlate = """<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <!-- linking css -->
        <link rel="stylesheet" href="css/style.css">
    </head>
    
    <body>
        <!-- Body starts here -->
        
        <!-- linking js -->
        <script src="js/script.js"></script>
    </body>

</html>
"""

# Programs stars here
print("Welcome to the automatic website folder structure creator.")
path = ""

while not os.path.isdir(path):
    # asking user to enter directory till user enters a valid one
    path = input("Enter directory: ")
    if not os.path.isdir(path):         #if directory does not exists
        print("Directory does not exist.")

# creating folders: images, css and js
createFolder("images")
createFolder("css")
createFolder("js")

# creating files in respective folders
createFile("style.css", "css")
createFile("script.js", "js")
createFile("index.html")

# adding a basic boiler plate to html file
writeToFile(os.path.join(path, "index.html"), html_boilerPlate)
print("HTML boiler plate created successfully.")

# exiting the program
input("Press any key to exit ")
