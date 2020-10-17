import requests
from bs4 import BeautifulSoup

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE = '\33[94m'
    WARNING = '\033[93m'

print (colors.BLUE + "__        __   _            ____                    _            ")
print ("\ \      / /__| |__        / ___|_ __ __ ___      _| | ___ _ __  ")
print (" \ \ /\ / / _ \ '_ \ _____| |   | '__/ _` \ \ /\ / / |/ _ \ '__| ")
print ("  \ V  V /  __/ |_) |_____| |___| | | (_| |\ V  V /| |  __/ |    ")
print ("   \_/\_/ \___|_.__/       \____|_|  \__,_| \_/\_/ |_|\___|_|    " + colors.STOP)
print

def main():
    URL = input(colors.GREEN + "WEBSITE : " + colors.STOP)

    print (colors.WARNING)

    r =requests.get(URL)
    soup = BeautifulSoup(r.content)
    dir_links = {}
    i = 0
    for a in soup.find_all('a', href=True):
        t = a['href']
        if t.startswith("/"):
           s = t.rfind('/')
           dir_links[i] = t[:s]
           i += 1
        if t.startswith(URL):
           link = t[len(URL):]	
           index = link.rfind('/')
           dir_links[i] = link[:index]
           i += 1
    print (colors.STOP)

    link_list = list(dir_links.values())
    link_list = list(dict.fromkeys(link_list))

    print('\x1b[6;30;42m' + 'Directories on website: '+ URL + ' : ' + '\x1b[0m')
    print('\n' + colors.WARNING + str(len(link_list)) + " Directories Found!" + colors.STOP)
    for x in link_list:
        print (x)
    print (colors.RED + "-"*100 + colors.STOP)
   
main() 
