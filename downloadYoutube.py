from pytube import YouTube
import os

try:
    downloads = 0
    content = ""
    filename = "downloadPath.txt"

    userAction = input('Menu:\n1. Download video\n2. Download audio\n3. Change download path\n\n-> ')

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
        url = input("Enter the YouTube URL: ")
        
        yt = YouTube(url)
        
        print("\nTitle:", yt.title)
        print("Views:", yt.views)

        # Get the highest resolution stream
        print('\n   What to download\n 0 - audio    1 - video')
        answerType = input()
        if answerType == "0":
            yd = yt.streams.get_audio_only()
        else:
            yd = yt.streams.get_highest_resolution()
        
        # Download the video to the current directory
        print('\n   Where to download\n   1 - change folder')
        answerDownload = input()
        if answerDownload == "1":
            downloadPath = input('Please, enter your download path: ')
            yd.download(downloadPath)
        else:
            # yd.download('D:\DOWNLOADS')
            yd.download(getDownloadPath(filename))
        
        print("Download complete.")
    # -------

    if value == "":
        print("Looks like you are first time here.\nPlease, set download path, so I will know where to download files to.")
        content = input("\nSet download path: ")
        setDownloadPath(filename, content)
        print("Download path set to:", getDownloadPath(filename))
    else:
        print("Your current download path is:", getDownloadPath(filename))


    if downloads == 0:
        downloadVid()
        downloads = downloads + 1
    while True:
        userInput = input("Do you want to download more?\n    If yes type '1'\n    -> ")

        if userInput == "1":
            downloadVid()
        else:
            print("See ya!")
            break

except Exception as e:
    print("An error occurred:", str(e))