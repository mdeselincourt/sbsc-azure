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

metadataUrl = 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fstorage.azure.com%2F'
metadataHeaders = {'Metadata': 'true'}
metadataRequest = requests.get(metadataUrl, headers=metadataHeaders) # headers=x
metadata=metadataRequest.text
metadataJson = metadataRequest.text

access_token = metadataRequest['access_token']

print(access_token)

exit(99) ## XXXXXXXXXXXXXXX

print("Getting blob")

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiJodHRwczovL3N0b3JhZ2UuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2VlMWQ4OThjLTBhNjQtNGIxMy05NTZkLWI4NDUyYjEwZmRhYy8iLCJpYXQiOjE2MTI4MDM2MjUsIm5iZiI6MTYxMjgwMzYyNSwiZXhwIjoxNjEyODkwMzI1LCJhaW8iOiJFMlpnWUxoUjZ2YTc5ZnhEdnVuVFo3RjlidjVUQ1FBPSIsImFwcGlkIjoiMGExOGY5MzAtYWMxZi00YmU5LWE2MWUtNzM5NmU5YTMzOWNkIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZWUxZDg5OGMtMGE2NC00YjEzLTk1NmQtYjg0NTJiMTBmZGFjLyIsIm9pZCI6IjYzNDBlYWY1LWFkOWUtNGMyMC04MDBmLTVlMTk3NzQ0YzY4MiIsInJoIjoiMC5BQUFBaklrZDdtUUtFMHVWYmJoRkt4RDlyREQ1R0FvZnJPbExwaDV6bHVtak9jMkJBQUEuIiwic3ViIjoiNjM0MGVhZjUtYWQ5ZS00YzIwLTgwMGYtNWUxOTc3NDRjNjgyIiwidGlkIjoiZWUxZDg5OGMtMGE2NC00YjEzLTk1NmQtYjg0NTJiMTBmZGFjIiwidXRpIjoiOE9IUkFONEM4RTZxbDViN0thTVRBQSIsInZlciI6IjEuMCIsInhtc19taXJpZCI6Ii9zdWJzY3JpcHRpb25zLzVjNmRkMDAyLTNhMjgtNGNiZS04ZGUzLTYxMDIxOTY3ZmY2NS9yZXNvdXJjZWdyb3Vwcy9yZy1zYnNjL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvdm0tYjFscy1zYnNjLXVrc291dGgtMDAxIn0.nDIkVrDUhuWFO1aIV3MS1qbc9eWouRGwawnZia8zQvoIzTmJDUcluTMR5vIeCAFdh7D_0ryU6OR246vEEIziML3SXUUro2DYf3MJr48Dh7Q7ZzCNDOlxkx0qa_AeAv_q6aWHxao__t9R2gJj-lLENFsSf4GbI2poRPMe8IX0gnjOvSPYvp-wlxX7n39qDAtR0By4FtYCrUU16iz40t0B55BcDQufhJ-gPk9tJbmjswXT-CxJ8P8g7TNuM73tAghkBE78g0Msj2izUSiYskequ6oVd0h5amyjxL_gR2HN4YCqqahdAajBsGcR2vhFftsntavuSEREqupKp220nL54lg',
    'Metadata': 'true',
    'x-ms-version': '2017-11-09'
}
blobUrl = 'https://sbsc.blob.core.windows.net/blob-container-sbsc-weather/weather-log.json'
request = requests.get(blobUrl, headers=headers) # headers=x


# -H "x-ms-version: 2017-11-09" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiJodHRwczovL3N0b3JhZ2UuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2VlMWQ4OThjLTBhNjQtNGIxMy05NTZkLWI4NDUyYjEwZmRhYy8iLCJpYXQiOjE2MTI4MDM2MjUsIm5iZiI6MTYxMjgwMzYyNSwiZXhwIjoxNjEyODkwMzI1LCJhaW8iOiJFMlpnWUxoUjZ2YTc5ZnhEdnVuVFo3RjlidjVUQ1FBPSIsImFwcGlkIjoiMGExOGY5MzAtYWMxZi00YmU5LWE2MWUtNzM5NmU5YTMzOWNkIiwiYXBwaWRhY3IiOiIyIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvZWUxZDg5OGMtMGE2NC00YjEzLTk1NmQtYjg0NTJiMTBmZGFjLyIsIm9pZCI6IjYzNDBlYWY1LWFkOWUtNGMyMC04MDBmLTVlMTk3NzQ0YzY4MiIsInJoIjoiMC5BQUFBaklrZDdtUUtFMHVWYmJoRkt4RDlyREQ1R0FvZnJPbExwaDV6bHVtak9jMkJBQUEuIiwic3ViIjoiNjM0MGVhZjUtYWQ5ZS00YzIwLTgwMGYtNWUxOTc3NDRjNjgyIiwidGlkIjoiZWUxZDg5OGMtMGE2NC00YjEzLTk1NmQtYjg0NTJiMTBmZGFjIiwidXRpIjoiOE9IUkFONEM4RTZxbDViN0thTVRBQSIsInZlciI6IjEuMCIsInhtc19taXJpZCI6Ii9zdWJzY3JpcHRpb25zLzVjNmRkMDAyLTNhMjgtNGNiZS04ZGUzLTYxMDIxOTY3ZmY2NS9yZXNvdXJjZWdyb3Vwcy9yZy1zYnNjL3Byb3ZpZGVycy9NaWNyb3NvZnQuQ29tcHV0ZS92aXJ0dWFsTWFjaGluZXMvdm0tYjFscy1zYnNjLXVrc291dGgtMDAxIn0.nDIkVrDUhuWFO1aIV3MS1qbc9eWouRGwawnZia8zQvoIzTmJDUcluTMR5vIeCAFdh7D_0ryU6OR246vEEIziML3SXUUro2DYf3MJr48Dh7Q7ZzCNDOlxkx0qa_AeAv_q6aWHxao__t9R2gJj-lLENFsSf4GbI2poRPMe8IX0gnjOvSPYvp-wlxX7n39qDAtR0By4FtYCrUU16iz40t0B55BcDQufhJ-gPk9tJbmjswXT-CxJ8P8g7TNuM73tAghkBE78g0Msj2izUSiYskequ6oVd0h5amyjxL_gR2HN4YCqqahdAajBsGcR2vhFftsntavuSEREqupKp220nL54lg"

print(request.text)

exit(99) ## XXXXXXXXXXXXXX

apikey = os.environ.get("WEATHER_API_KEY")

import urllib.request
url = 'http://api.openweathermap.org/data/2.5/weather?id=2643743&appid={appid}'.format(appid=apikey)
# url.format(appid=apikey)
print(url)
with urllib.request.urlopen(url) as response:
    print(str(response))
    weather = json.loads(response.read().decode())
    wind = weather["wind"]
    # print(weather["wind"])

now = time.time()

log=json.loads('{"history":{}}')

log["history"][now]=weather

print(log)