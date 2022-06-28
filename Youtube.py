from pytube import YouTube

class YoutubeDownloader():

    link = input('Enter the link of youtube video you want to download:')
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()

    def __init__(self,Author):
        self.Author = Author

    def video_Title(self):
        Title = self.yt.title
        print('Title:{}'.format(Title))

    def VIEWS(self):
        views = self.yt.views
        print('Number of views : {}'.format(views))

    def Length(self):
        length = self.yt.length
        print('Lenght of video : {}'.format(length))

    def Ratings(self):
        video_ratings = self.yt.rating 
        print('Rating of video : {}'.format(video_ratings))

    def Download(self):
        target = self.ys
        print('Downloading....')
        path = 'C:\\Users\\User\\OneDrive\\Desktop\\YouTube'
        target.download(path)
        print('Download completed!') 

MyYoutubeDownloader = YoutubeDownloader('Emmanuel')

MyYoutubeDownloader.Ratings()
MyYoutubeDownloader.VIEWS()
MyYoutubeDownloader.Length()
MyYoutubeDownloader.video_Title()
MyYoutubeDownloader.Download()




