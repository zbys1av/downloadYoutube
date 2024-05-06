from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    print('Video file will be downloaded, if you need audio file - type "audio"')
    answerType = input()
    if answerType == "audio":
        yd = yt.streams.get_audio_only()
    else:
        yd = yt.streams.get_highest_resolution()
    print('Loading...')
    
    # Download the video to the current directory
    print('If you want to change download folder type "1"')
    answerDownload = input()
    if answerDownload == "1":
        print('Please, enter your download path')
        downloadPath = input()
        yd.download(downloadPath)
    else:
        yd.download('D:\DOWNLOADS')
    print('Downloading...')
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))