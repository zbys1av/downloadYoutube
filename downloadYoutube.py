from pytube import YouTube
import os

try:
    downloads = 0
    content = ""
    filename = "downloadPath.txt"

    # -------
    def downloadMenu():
        userAction = input('\nMenu:\n1. Download video\n2. Download audio\n3. Change download path\n\n-> ')

        if userAction == "1":
            downloadVid()
            # downloads = downloads + 1
        elif userAction == "2":
            downloadAudio()
            # downloads = downloads + 1
        elif userAction == "3":
            content = input("\nSet download path: ")
            setDownloadPath(filename, content)
            print(f"Download path set to: {getDownloadPath(filename)}\n")
            downloadMenu()
        else:
            print("Incorrect input. Try again")
            downloadMenu()
    # -------
    def getDownloadPath(filename):
        try:
            with open(filename, 'r') as file:
            # Read the first line
                value = file.readline().strip()
                return value
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None
    # -------
        
    value = getDownloadPath(filename)

    # -------
    def setDownloadPath(filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except Exception as e:
            print(f"Error writing to file '{filename}': {e}")
    # -------

    # -------
    def downloadVid():
        # Ask the user to input the YouTube URL
        url = input("\nEnter the YouTube URL: ")
        
        yt = YouTube(url)
        
        print("\nTitle:", yt.title)
        print("Views:", yt.views)

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()
        yd.download(getDownloadPath(filename))
        # downloads = downloads + 1
        print("\nDOWNLOAD COMPLETED")
    # -------

        # -------
    def downloadAudio():
        # Ask the user to input the YouTube URL
        url = input("\nEnter the YouTube URL: ")
        
        yt = YouTube(url)
        
        print(f"\nTitle: {yt.title}")
        print(f"Views: {yt.views}\n")
        
        yd = yt.streams.get_audio_only()
        yd.download(getDownloadPath(filename))
        # downloads = downloads + 1
        print("\nDOWNLOAD COMPLETED")
    # -------

    if value == "":
        print("Looks like you are first time here.\nPlease, set download path, so I will know where to download files to.")
        content = input("\nSet download path: ")
        setDownloadPath(filename, content)
        print(f"Download path set to: {getDownloadPath(filename)}\n")
    else:
        print(f"Your current download path is: {getDownloadPath(filename)}", )

    # userAction = input('Menu:\n1. Download video\n2. Download audio\n3. Change download path\n\n-> ')
    downloadMenu()

    while True:
        userInput = input("\n1. Download more\n2. Exit\n-> ")
        if userInput == "1":
            downloadMenu()
        else:
            print("\nSee ya! \nYou can close this window now ;)")
            break

except Exception as e:
    print("An error occurred:", str(e))