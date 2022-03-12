# Installing pytube in your Terminal: pip install pytube

# Importing the module:
from pytube import YouTube

# Link of the video to be downloaded:
URL_VIDEO = input('Input the url of the video: ')
yt = YouTube(URL_VIDEO)

# Get the video with the highest resolution:
video_highest_res = yt.streams.get_highest_resolution()

try:
    # Downloading and saving the video: modify backslash to forward slash
    video_highest_res.download(output_path = 'C:/Users/example/Videos/')
except: 
    print('Some Error!')
print('Download Completed!')
