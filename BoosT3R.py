#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BoosT3R FrameWork
~~~~~~~~

Framework for Use Attacks , Pentests and ...
"""

# Download fileUpio
execT = open('Core/downloader.txt').read()
exec(execT)

#----[ import Base libraries ]----
import time 
import os
import fileUpio.fileio

#----[ import Boosts Module ]----
import BoosT3RSettings as BS
import BoosT3RColors as BC
import BoosT3RConnections as BCC

#----[ set Values for Better Access ]----
box = BS.Box
animation = BS.Animation
settings = BS
colors = BC.colors
prefixes = BC.prefixes
pool = BCC.PoolConnections
aiBoosT3R = BCC.AI
reader = BS.Reader

#----[ show Colors for Windows Users ]----
os.system('')


#----[ class and Functions ]----
class C:
    
    def A():
        launchTime = time.strftime('%H:%M:%S')
        settings.Active = True
        animation.ani(f'{colors.white}[{colors.cyan}{launchTime}{colors.white}] [{prefixes.META_INFO}{colors.white}] {colors.yellow}Check for updates', 1)
        starterTime = time.strftime('%H:%M:%S')
        print()
        print(box('Welcome to Booster, for see results type " help "').infoMessageBox(starterTime))
            
        while 1:
            user = str(input(f'\n{colors.yellow}[{colors.darkblue}λ{colors.yellow}] {colors.white}{colors.underline}{colors.white}Boost3r{colors.cyan} >{colors.white} '))
            
            if user == "help":
                helpTime = time.strftime('%H:%M:%S')
                print(box('Will Be Soon ...').infoMessageBox(helpTime))
            
            elif "pool" in user.split():
                poolHelpTime = time.strftime('%H:%M:%S')
                print(box('Welcome to Pool Class, you can Start A pool like:\n\nfor Method " GET " => pool-get https://www.example.com\nget status =>         pool-get https://www.example.com --status\nget json =>           pool-get https://www.example.com --json\n\nfor Method " POST " => pool-post ...').infoMessageBox(poolHelpTime))
            
            elif "pool-get" in user.split():
                if user.split()[-1] == "--status":
                    url_ = user.split()[user.split().index('pool-get')+1]
                    data = pool(url=url_).getConnectionStatus()
                    pTime = time.strftime('%H:%M:%S')
                    print()
                    print(box(data).infoMessageBox(pTime))
                
                elif user.split()[-1] == "--json":
                    urlj_ = user.split()[user.split().index('pool-get')+1]
                    data2 = pool(url=urlj_).getConnectionJson()
                    p2Time = time.strftime('%H:%M:%S')
                    print()
                    print(box(data2).infoMessageBox(p2Time))
                    
                else:
                    urlDif_ = user.split()[user.split().index('pool-get')+1]
                    datad = pool(url=urlDif_).getConnectionStatus()
                    dpTime = time.strftime('%H:%M:%S')
                    print()
                    print(box(datad).infoMessageBox(dpTime))
                    
            elif "pool-post" in user.split():
                if user.split()[-1] == "--status":
                    url_ = user.split()[user.split().index('pool-post')+1]
                    data = pool(url=url_).postConnectionStatus()
                    pTime = time.strftime('%H:%M:%S')
                    print()
                    print(box(data).infoMessageBox(pTime))
                
                elif user.split()[-1] == "--json":
                    urlj_ = user.split()[user.split().index('pool-post')+1]
                    data2 = pool(url=urlj_).postConnectionJson()
                    p2Time = time.strftime('%H:%M:%S')
                    print()
                    print(box(data2).infoMessageBox(p2Time))
                    
                else:
                    urlDif_ = user.split()[user.split().index('pool-post')+1]
                    datad = pool(url=urlDif_).postConnectionStatus()
                    dpTime = time.strftime('%H:%M:%S')
                    print()
                    print(box(datad).infoMessageBox(dpTime))

            elif user.startswith("ai"):
                text = user.replace('ai ', '')
                
                if text == 'ai':
                    errorAiTime = time.strftime('%H:%M:%S')
                    print(box('Faild To use: ai Hello How Are You?').errorMessageBox(errorAiTime))
                    
                else:
                    newText = text.replace(' ', '+')
                    dataGPT = aiBoosT3R.chatGPT(text=newText)
                    gptTime = time.strftime('%H:%M:%S')
                    print(box(f"""
Question: {text}

Answer: {dataGPT}

""").infoMessageBox(gptTime))
                    
            elif "open" in user.split():
                if len(user.split()) == 1:
                    openError = time.strftime('%H:%M:%S')
                    print()
                    print(box('Faild To use: open #<file name or path to a file to read>').errorMessageBox(openError))
                
                else:
                    if user.split()[-1] == "-rs" or user.split()[-1] == "--read-simple":
                        fileOrPathSimpleRead = user.split()[user.split().index('open')+1]
                        simpReadTime = time.strftime('%H:%M:%S')
                        print()
                        print(box(f"\n{reader(fileNameOrPath=fileOrPathSimpleRead).read()}").infoMessageBox(simpReadTime))
                    
                    elif user.split()[-1] == '-rb' or user.split()[-1] == '--read-binery':
                        fileOrPathBinRead = user.split()[user.split().index('open')+1]
                        binReadTime = time.strftime('%H:%M:%S')
                        print()
                        print(box(f"\n{reader(fileNameOrPath=fileOrPathBinRead, typeToRead='rb').read()}").infoMessageBox(binReadTime))
                    
                    else:
                        fileOrPathDif= user.split()[user.split().index('open')+1]
                        difReadTime = time.strftime('%H:%M:%S')
                        print()
                        print(box(f"\n{reader(fileNameOrPath=fileOrPathDif).read()}").infoMessageBox(difReadTime))
                        
            elif "upload" in user.split():
                if len(user.split()) == 1:
                    uploaderTimeError = time.strftime('%H:%M:%S')
                    print(
                        box('Faild to use: upload #<file name or path to a file to upload>').errorMessageBox(uploaderTimeError)
                    )
                else:
                    fileNameOrPathToUp = user.split()[user.split().index('upload')+1]
                    timeToUp = time.strftime('%H:%M:%S')
                    print(box('').infoMessageBox(timeToUp))
                    fileUpio.fileio.FileUploader(fileNameOrPathToUp).upload()

            
            elif user == "exit":
                exit(0)
                
            else:pass

C.A()
