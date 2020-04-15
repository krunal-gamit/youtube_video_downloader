from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

FolderName = ""
fileSizeInBytes = 0
MaxFileSize = 0


def openDirectory():
    global FolderName
    FolderName = filedialog.askdirectory()
    if (len(FolderName) > 1):
        fileLocationLabelError.config(text=FolderName,
                                      fg="green")

    else:
        fileLocationLabelError.config(text="Please choose folder!",
                                      fg="red")


def DownloadFile():
    global MaxFileSize, fileSizeInBytes

    choice = youtubeChoices.get()
    video = youtubeEntry.get()

    if (len(video) > 1):
        youtubeEntryError.config(text="")
        print(video, "at", FolderName)
        yt = YouTube(video, on_progress_callback=progress)
        print("Video Name is:\n\n", yt.title)

        if (choice == downloadChoices[0]):
            print("720p Video file downloading...")
            loadingLabel.config(text="720p Video file downloading...")  #

            selectedVideo = yt.streams.filter(progressive=True).first()

        elif (choice == downloadChoices[1]):
            print("144p video file downloading...")
            selectedVideo = yt.streams.filter(progressive=True,
                                              file_extension='mp4').last()

        elif (choice == downloadChoices[2]):
            print("3gp file downloading...")
            selectedVideo = yt.streams.filter(file_extension='3gp').first()

        elif (choice == downloadChoices[3]):
            print("Audio file downloading...")
            selectedVideo = yt.streams.filter(only_audio=True).first()

        fileSizeInBytes = selectedVideo.filesize
        MaxFileSize = fileSizeInBytes / 1024000
        MB = str(MaxFileSize) + " MB"
        print("File Size = {:00.00f} MB".format(MaxFileSize))

        # now Download ------->
        selectedVideo.download(FolderName)
        # ==========>
        print("Downloaded on:  {}".format(FolderName))
        complete()

    else:
        youtubeEntryError.config(text="Please paste YouTube link",
                                 fg="red")
    # ============progress bar==================


def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # Gets the percentage of the file that has been downloaded.
    # nextLevel = Toplevel(root)
    percent = (100 * (fileSizeInBytes - remaining)) / fileSizeInBytes
    print("{:00.0f}% downloaded".format(percent))
    # loadingLabel.config(text="Downloading...")


def complete():
    loadingLabel.config(text=("Download Complete"))


# ================tkinter window
root = Tk()
root.title("Youtube Video downloader")
# ===============contents strech ac to windows strech====
root.grid_columnconfigure(0, weight=1)  # strech things Horiontally
# =============youtube link label=================
youtubeLinkLabel = Label(root,
                         text="Paste the YouTube link: ",
                         fg="blue", font=("Raleway", 20,"bold"))
youtubeLinkLabel.grid()
# ==========get youtube link in entry box
youtubeEntryVar = StringVar()
youtubeEntry = Entry(root, width=50,
                     textvariable=youtubeEntryVar)
youtubeEntry.grid(pady=(0, 20))
# =========when link is wrong print this label
youtubeEntryError = Label(root, fg="red",
                          text="", font=("Raleway", 20))
youtubeEntryError.grid(pady=(0, 10))

# Asking where to save file label
SaveLabel = Label(root,
                  text="Destination: ", fg="blue",
                  font=("Arial", 20, "bold"))
SaveLabel.grid()
# Asking where to save file Button
SaveEntry = Button(root, width=20, bg="green", fg="white",
                   text="Choose folder", font=("arial", 15),
                   command=openDirectory)
SaveEntry.grid()

# Entry label if user don`t choose directory
fileLocationLabelError = Label(root,
                               text="", font=("Agency FB", 20))
fileLocationLabelError.grid(pady=(0, 0))
# ======= what to download choice==========
youtubeChooseLabel = Label(root,
                           text="Please choose what to download: ",
                           font=("Agency FB", 20))
youtubeChooseLabel.grid()

# Combobox with four choices:
downloadChoices = ["MP4_720p",
                   "Mp4_144p",
                   "Video_3gp",
                   "Song_MP3"]

youtubeChoices = ttk.Combobox(root, values=downloadChoices)
youtubeChoices.grid()

# ==================Download button===================
downloadButton = Button(root,
                        text="Download", width=15, bg="green",
                        command=DownloadFile)
downloadButton.grid(pady=(20, 20))
# Progressbar ======>
progressbar = ttk.Progressbar(root, orient="horizontal",
                              length=500, mode='indeterminate')
progressbar.grid(pady=(2, 0))

loadingLabel = ttk.Label(root, text="18bce063,18bce066,18bce067",
                         font=("Raleway", 10))
loadingLabel.grid()

root.mainloop()
