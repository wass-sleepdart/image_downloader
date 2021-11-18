import requests
import json
import os
import wget
import time
#You need to get an api key for this to work 
#you can get a free aoi key here:'https://unsplash.com/documentation'
#once you get the api key put it after the client_id= in the url
url='https://api.unsplash.com/photos/random/?client_id='

def get_image(topic, count):
        wallpapers_folder=os.chdir('C:\Wallpapers')
        headers={
        'Accept-Version': 'v1',
        }
        parameters={
        'query':str(topic),
        'count':count
        }
        data=requests.get(url=url, headers=headers, params=parameters)
        json_file=data.text
        json_to_dict=json.loads(json_file)
        image_url=json_to_dict[0]['urls']['raw']
        wget.download(image_url, topic+'.jpg')

get_image('desktop wallpapers',3)


  

