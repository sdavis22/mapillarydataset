import os
import requests
import json
import reverse_geocode
import shutil

def main():
    dirPath = "dataset/mapillary/training/images"
    directory = os.fsencode(dirPath)
   # geolocator = Nominatim(user_agent="myGeocoder")
    dircontents = os.listdir(directory)
    count = 0
    epoch = 0 #This isn't really an epoch as much as it is progress, but in the spirit of neural nets
    for file in sorted(dircontents):
        #Get file metadata
        fileName = os.fsdecode(file)
        filePath = os.path.join(dirPath, fileName)
        if fileName.endswith(".jpg"): 
            #Get coordinates from the image json
            imageName = fileName.replace('.jpg', '')
            url = "https://a.mapillary.com/v3/images/"
            url += imageName + "?client_id=N0ZMR1VPa0pTa1VJck1xM2RDMDA0ejo4M2IwMDE3YjJkMTJiMjcw"
            failure = True
            while(failure):
                try:
                    imageData = requests.get(url).json()
                    latitude = imageData['geometry']['coordinates'][0]
                    longitude = imageData['geometry']['coordinates'][1]
                    coords = (latitude, longitude), (0,0)
                    failure = False
                except:
                    failure = True
                    print("Help im stuck at ", imageName)
            #For some reason, there has to be at least two coordinates to every ping, so I just did
            # 0,0 as the second, since I didn't feel like dealing with loading 2 files
            location = reverse_geocode.search(coords)
            country = location[0]['country'] 
            countryFolder = os.path.join(dirPath, country)
            countryFile = os.path.join(countryFolder, fileName)
            #If there's not a folder with the country name, create one
            if(os.path.exists(countryFolder)):
                if(not os.path.isdir(countryFolder)):
                    os.mkdir(countryFolder)
            else:
                os.mkdir(countryFolder)
            #Add the image to the corresponding country folder
            shutil.move(filePath, countryFile)
            count+=1
            if(count == 100):
                count = 0
                epoch+= 1
                print("epoch: " + str(epoch) + "/ 180")
            

main()