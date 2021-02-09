try:
    # Native
    import json # 
    import time # For timestamping data
    import os, uuid # For access to API key and for Az blob storage
    
    # External
    import requests
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

except:
    print ("You need requests, azure.storage.blob installed")

# print("Azure Blob Storage v" + __version__)

### GET METADATA ABOUT SELF (AZURE VM)

print("Getting metadata")

accessToken = False

try:
    metadataUrl = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fstorage.azure.com%2F'
    metadataHeaders = {'Metadata': 'true'}
    metadataRequest = requests.get(metadataUrl, headers=metadataHeaders, timeout=1.0) # headers=x
    metadataString = metadataRequest.text
    metadataJson = json.loads(metadataString)
    accessToken = metadataJson['access_token']
except:
    print("Could not get own metadata...")

print("Getting blob")

if accessToken:
    # Prepare to make request
    headers = {
        'Authorization': 'Bearer ' + accessToken,
        'Metadata': 'true',
        'x-ms-version': '2017-11-09'
    }
    blobUrl = 'https://sbsc.blob.core.windows.net/blob-container-sbsc-weather/weather-log.json'
    # Make request
    request = requests.get(blobUrl, headers=headers) # headers=x
    # Turn response into a JSON object
    weatherHistoryObject = json.loads(request.text)
else:
    print("Falling back to BLOB_CONNECTION_STRING)")
    # Prepare to make request
    blobConnectionString = os.environ.get("BLOB_CONNECTION_STRING")
    if blobConnectionString:
        print("blobConnectionString found")
        blobClient = BlobClient.from_connection_string(conn_str=blobConnectionString, container_name="blob-container-sbsc-weather", blob_name="weather-log.json")
        # Get data
        blob_data = blobClient.download_blob().readall()
        weatherHistoryObject = json.loads(blob_data.decode('utf8'))
    else:  
        print("Error - No BLOB_CONNECTION_STRING")
        exit(1)

print(weatherHistoryObject)

exit(99)

apikey = os.environ.get("WEATHER_API_KEY")

import urllib.request
url = 'http://api.openweathermap.org/data/2.5/weather?id=2643743&appid={appid}'.format(appid=apikey)
# url.format(appid=apikey)
print(url)
with urllib.request.urlopen(url) as response:
    print(str(response))
    weatherObject = json.loads(response.read().decode())
    windObject = weatherObject["wind"]
    # print(weather["wind"])

now = time.time()

weatherHistoryObject["history"][now]=weatherObject

print(log)