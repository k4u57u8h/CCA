import requests
import zipfile
URL = "https://storage.googleapis.com/kaggle-data-sets/426827/1031720/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1586631827&Signature=JhGWrIOFw5t9AryYR4tkXebqf%2FMtOevs8B4Ir9fTjYSPhbVknQJt98gad3NJM%2FSGhCn%2BcOCkFDawIGD8fck%2F3hoROM1hYexq5Y5G7UHC7XUO6h96nVDM2yDTAG0e6IqZbutO33dtjpPPWxhOOEOy1iWkbD4YGjoivBSvexhjavBwFYaERemGmibbAN2FmjiYhPk5AoBwtN4f9Jc31%2BolJqFprmVOMzSus4sxad5I%2Bnd1KF4K8FTxZOHf3IpO7rT%2Fdc3OiYJq64LC%2F%2F42gfkEeyb5YYK3vR%2FNSqf3Wuir835ks8gOQOk%2BpE3fZKiEkvNt2lwuEuj4HXsLbo4rcjrY7A%3D%3D&response-content-disposition=attachment%3B+filename%3Dcredit-card-approval-prediction.zip"
  
r = requests.get(URL, stream = True) 
  
with open("data.zip","wb") as f:
    print("Please wait while your data is being saved ....")
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

with zipfile.ZipFile('data.zip', 'r') as zip_ref:
    zip_ref.extractall('')

print("File saved successfully.")
