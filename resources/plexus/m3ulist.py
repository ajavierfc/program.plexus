# -*- coding: utf-8 -*-

""" 2018 ajavierfc

    This brings the ability to load a links list and play the links (acestream:// or .torrent)
    
    Functions:
    
    load_m3u() -> Locate and display a .m3u or .m3u8 file
       

"""
    
import xbmcgui,re
from plexusutils.directoryhandle import addDir

def load_m3u():
    file = xbmcgui.Dialog().browse(1, 'Find M3U file','video', '.m3u|.m3u8')
    if file:
        lines = open(file, 'r').readlines()
        for line in lines:
            if '#EXTINF' == line[0:7]:
                info=re.sub('^[^,]+,','',line)
            elif 'acestream://' == line[0:12] or '.torrent' in line:
                addDir(info.strip(),line.strip(),1,'',1,False)
    else: pass
