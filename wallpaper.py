import json
import urllib.request
import ctypes

data = urllib.request.urlopen("https://api.unsplash.com/photos/random?client_id=d5c6d253d613de43d6e94d7a3a8507076fbe1c9c0fe3f183469c360082841306").read()
output = json.loads(data)
temp_file_name = "C:\\python-projs\\imgs_folder\\background.jpg"
img_dir_link = output["urls"]["full"];
# save the gotten imaged to local
print ("Downloading image...")
urllib.request.urlretrieve(img_dir_link,temp_file_name)
print ("Image save as "+temp_file_name);
print ("Setting Image as wall paper")
ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_file_name , 0)
print (img_dir_link)