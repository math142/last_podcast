from selenium.webdriver.remote.webdriver import WebDriver
from web import *
import subprocess
import os.path
from os import path
import time 
def main():
    titre = []
    if mounted_nas():
        driver = configuration()
        info = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,'video-title')))
        for i in range(len(info)):
            if path.isfile('/home/nas/kino+/{}'.format(info[i].text)):
                continue
            else:
                link = info[i].get_attribute('href')
                download(link)
                handle_file(info[i].text)
    
def mounted_nas():
    nbrFolder = subprocess.check_output('find /home/nas -maxdepth 1 -type d|wc -l',shell=True) 
    nbrFolder = int(nbrFolder)
    if nbrFolder > 1:
        return True
    else:
        return False
def download(link):
    subprocess.call('python3 /home/mathieu/last_podcast/yt-dlp {}'.format(link),shell=True).wait()
    
def handle_file(filename):
    os.system('sudo cp /home/mathieu/last_podcast/{}.webm /home/nas/Kino+/'.format(filename))
    os.system('sudo rm /home/mathieu/last_podcast/{}.webm'.format(filename))

if  __name__ == '__main__':
    main()
    
