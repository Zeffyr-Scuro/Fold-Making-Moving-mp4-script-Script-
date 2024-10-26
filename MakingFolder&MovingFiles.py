import os

def MakingFolders(source, destination):

    try:

        sourceDir = os.listdir(source)

    except PermissionError:
        print(f"Permission denied: Unable to access {sourceDir}")

    except Exception as error:
        print(f"An error occurred: {error}")

    for file in sourceDir:

        # Stoping the hidden file for making there own folders
        if file[0] == ("."):
            pass
        else:
            # Making sure only files ending in .mp4 are coming though
            if file.endswith(".mp4"):
                
                # Creating the new Directorys name from the Files name
                newDirName = os.path.join(destination, file.replace(".mp4", ""))

                # Try to make new Directory
                try:

                    os.makedirs(newDirName)

                except FileExistsError:
                    print(f"Directory {newDirName} already exists")

                except PermissionError:
                    print(f"Permission denied: Unable to create {newDirName}")

                except Exception as error:
                    print(f"An error occurred: {error}")

                # Try to move file to the new Directory
                try:

                    os.rename(f"{os.path.join(source, file)}", f"{os.path.join(newDirName, file)}")

                except FileExistsError:
                    print(f"{file} already exists in {newDirName}")

                except PermissionError:
                    print(f"Permission denied: Unable to move {file}")

                except Exception as error:
                    print(f"An error occurred: {error}")
                

                # Try to move the hidden file to the new Directory
                try:

                    os.rename(f"{os.path.join(source, "._"+file)}", f"{os.path.join(newDirName, "._"+file)}")

                except FileExistsError:
                    print(f"._{file} already exists in {newDirName}")

                except PermissionError:
                    print(f"Permission denied: Unable to move ._{file}")

                except Exception as error:
                    print(f"An error occurred: {error}")
        

def Setup():
    print("If you wan to Exit. type EXIT")
    sourceDirNotValid = True
    destinationDirNotValid = True
    pathwayExample = os.path.join(os.path.expanduser('~'), "Desktop")

    while sourceDirNotValid:
        # Asking for source Directory
        sourceDir = input("Where are the files you want to make folders for located: ")
        # Exit script
        if sourceDir.upper() == "EXIT":
            raise SystemExit
        
        elif os.path.exists(sourceDir):
            sourceDirNotValid = False
           
        else:
            print(f"{sourceDir} does not exist. Please enter a valid Pathway Like {pathwayExample}")
    
    while destinationDirNotValid:
            
         #Asking for destination Directory or to use the same as source Directory
            destinationDir = input(f"Where do you want to make the new folders press Enter if you want them in placed in {sourceDir} or 1 for Custom pathway: ")

            # Exit script
            if destinationDir.upper() == "EXIT":
                raise SystemExit
            
            elif destinationDir == "1":
                destinationDir = input("Enter Cutom pathway: ")

            else:
                destinationDir = sourceDir
            
            if os.path.exists(destinationDir):
                
                destinationDirNotValid = False
                MakingFolders(sourceDir, destinationDir)
            
            else:
                print(f"{destinationDir} does not exist. Please enter a valid Pathway Like {pathwayExample}")

Setup()