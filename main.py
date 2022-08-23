from pytube import YouTube

url = input("Enter url: ")
my_video = YouTube(url)

print(f"Video Title: {my_video.title}")

print(f"Downloading...")
my_video = my_video.streams.get_highest_resolution()
my_video.download()
print("Video Downloaded!")