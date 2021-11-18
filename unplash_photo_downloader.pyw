import requests
import json
import os
import wget
import time
url='https://api.unsplash.com/photos/random/?client_id=QNFW-dI2vBRYt-7Ek5WcrWxNdabSiqWRJQ01Fn90WGc'

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

#get_image('desktop wallpapers',3)

def mymin(tocheck):
    minval = None
    for cur in tocheck:
        if minval is None or cur < minval:
            minval = cur
    return minval
print(mymin([1,-45,-54,-64,-456,3,4,55,667,58,23]))

  

