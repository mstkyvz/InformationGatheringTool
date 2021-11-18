#!/usr/bin/python3
#coding:utf-8

from libs.tools import *
from libs.banner import banner
from libs.clear import clear
import colorama,os
 
def main():
    while True:
       clear()
       banner()
       try:
          choose = input(colorama.Fore.RED+"     ┌─["+colorama.Fore.LIGHTGREEN_EX+" ElitHatZ.Com@walker835 "+colorama.Fore.RED+"]-["+colorama.Fore.GREEN+"Home"+colorama.Fore.RED+"""]
     └───# """+colorama.Fore.WHITE)
       except:
          pass
       if not choose:
          pass
       elif choose == "00":
          exit()
       elif choose == "1":
          cloudflarebypass()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "2":
          traceroute()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "3":
          cmsdetect()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "4":
          reverseip()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "5":
          portscan()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "6":
          httpheader()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "7":
          whois()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")   
       elif choose == "8":
          geoiplookup()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....") 
       elif choose == "9":
          dnslookup()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "10":
          findshareddns()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "11":
          robotstxt()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "12":
          adminpanelfinder()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "13":
          bannergrabbing()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "14":
          pagelinks()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "15":
          websiteonof()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "16":
          ipfind()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "17":
          subscan()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "18":
          zonetransfer()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "19":
          testping()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "20":
          reversedns()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "21":
          directoryfuzz()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "22":
          emailextractor()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "23":
          subnetlookup()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "24":
          nslookup()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "25":
          wpuserenumerate()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "26":
          alexacheck()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       elif choose == "27":
          cloudflaredetect()
          input(colorama.Fore.WHITE+"\n["+colorama.Fore.RED+"#"+colorama.Fore.WHITE+u"] Devam etmek için [ENTER]'a basın....")
       else:
          pass
if __name__=="__main__": 
    main()