from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from tkinter import filedialog
import datetime
import webbrowser
import pytube
from pytube import YouTube
import numpy

def main():                         #Kyroz                      #Smi77y                     #Ludwig                     #UnusualVideos              #Byze                       #Blarg                      #Vertasium                  #McNasty                    #Smii7yPlus                 #Soup                       #AlsoFitz                   #LessTeo                    #Storror                    #BOOS                       #BlargLive                  #TobyOnTheTele              #Fitz                       #TheDooo                    #ColdOnes                   #D!ng                       #BlargTv                    #Vsauce                     #MoreKryoz                  #I did a thing              #Mark Rober                 #PewDiePie                  #TheDoooTooo                #Teo                        #Kurzgesagt                 #YesTheory                  #SwaggerSouls               #Boy Boy                    #GoonsGaming                #Luke Kidgel                #Liam Thompson              #McNastier                  #Michael Reeves             #RaccoonEggs
    channel_id_array = numpy.array(["UCi-QR0jFereBXjU9SBxcdeg", "UCzXwjTI6c6mVn6oui_p6oiw", "UC4USoIAL9qcsx5nCZV_QRnA", "UCpnkp_D4FLPCiXOmDhoAeYA", "UCtBFqR-itrGB4C566GkfrTA", "UCorikuuyFz1dZLo3N9nHc4w", "UCHnyfMqiRRG1u-2MsSQLbXA", "UCvmWj7t7nP3yOSU_rl9doCQ", "UC-gW4TeZAlKm7UATp24JsWQ", "UCifRgVk-GEo1_vvf8x53t6A", "UCHXJ0dhS3NpTBFg7lR_5w8Q", "UCPNPv2AYNvQ5qdZo8KBKKFA", "UCdPui8EYr_sX6q1xNXCRPXg", "UCc0kHafEIzm6PiqyrsC5lyg", "UCj7KXMG2Bc4QAe1mSAOShtA", "UCEUJmFa1ItxuZg6RvlAwRYg", "UCtb8P4rf_1n8KS8eZk_lNNw", "UCPKgIhTC3BdkAwMw6s-GEug", "UCfbnTUxUech4P1XgYUwYuKA", "UClq42foiSgl7sSpLupnugGA", "UCBKhHQPLXQqru8Zs-5LwmiA", "UC6nSFpj9HTCZ5t-N3Rm3-HA", "UCX_fEsnSHXaJV2f2JjsDvow", "UCJLZe_NoiG0hT7QCX_9vmqw", "UCY1kMZp36IQSyNx_9h4mpCg", "UC-lHJZR3Gqxm24_Vd_AJ5Yw", "UCb3n4k6_smEbOUqiXu4rlOg", "UCDa8HbNrmkFhKKOeiB7JaRw", "UCsXVk37bltHxD1rDPwtNM8Q", "UCvK4bOhULCpmLabd2pDMtnA", "UCMdGPato0IC5-zZjJIf-P9w", "UC_S45UpAYVuc0fYEcHN9BVQ", "UCZbIPAVd6Zg9vs6Q4cRZisA", "UCcKvm2VL8xTInRggo8A3alA", "UCU5O8FCtOTI4BWhfHF2LHJw", "UCSKUNcjmYDX5A-KSxnNk7QQ", "UCtHaxi4GTYDpJgMSGy7AeSw", "UC9n8unUsC6coX-T0wmX5uPg"])
    #channel_id = 'YOUR_CHANNEL_ID'  # Replace with the desired YouTube channel ID
    api_key = 'AIzaSyAclZSKJXBqWuAvLSafyEV3Tc5201R08A8'  # Replace with your YouTube Data API key

    video_ids = get_latest_videos(channel_id_array, api_key)

    for channel_videos in video_ids:
        for video_id in channel_videos:
            if is_video_new(video_id):
                open_video(video_id)
    


def get_latest_videos(channel_id_array, api_key):
    try:
        video_ids = []
        youtube = build('youtube', 'v3', developerKey=api_key)
        for channel in channel_id_array:    
            request = youtube.search().list(
                part='snippet',
                channelId=channel,
                order='date',
                maxResults=1  # Adjust the number of videos you want to retrieve
            )
            response = request.execute()
            video_ids.append([item['id']['videoId'] for item in response['items']])
            #print(video_ids)
        return video_ids
    except HttpError as e:
        print('An HTTP error occurred:')
        print(e)
        return None
    
def open_video(video_id):
    webbrowser.open(f'http://youtube.com/watch?v={video_id}')

def is_video_new(video_id):
    try:  
        yt = pytube.YouTube(f'https://www.youtube.com/watch?v={video_id}')
        name = yt.title
        published_date = yt.publish_date
        current_datetime = datetime.datetime.now()
        difference = current_datetime - published_date
        if difference.days <= 1:
            return True
        else:
            return False
    except pytube.exceptions.VideoUnavailable:
        print(f"Video with ID '{video_id}' is unavailable.")
        return False



if __name__ == "__main__":
    main()