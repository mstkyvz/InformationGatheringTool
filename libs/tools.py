from multiprocessing.pool import ThreadPool
from libs.clear import clear
from colorama import init,Fore
import socket,requests,re,json,os
init()

def cloudflarebypass():
      clear()
      subdomainlist = ["ftp", "cpanel", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog", "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator", "email", "downloads", "ssh", "owa","bbs", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5","shop", "api", "blogs", "test","mx1","cdn", "mysql", "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support", "web", "dev"]
      host = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
      print("")
      for sublist in subdomainlist:
       try:
          hosts = str(sublist) + "." + str(host)
          showip = socket.gethostbyname(str(hosts))
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] CloudFlare Bypass "+str(showip)+' --> '+str(hosts))
       except:
            pass

def traceroute():
       clear()
       target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
       print("")
       r = requests.get("https://api.hackertarget.com/mtr/?q="+target).text
       print(r)
 
def cmsdetect():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
      print("")
      try:
       r = requests.get(target).text
       if "wordpress" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : WordPress")
       elif "opencart" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : OpenCart")
       elif "joomla" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : Joomla")
       elif "prestashop" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : PrestaShop")
       elif "drupal" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : Drupal")
       elif "vbulletin" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : Vbulletin")
       elif "xenforo" in r:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Cms : XenForo")
       else:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : "+target)
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+u"] Cms : Bulunamadı")  
      except:
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+u"] Siteye erişilemiyor!")       
          
def reverseip():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
      print("")
      r = requests.get("https://api.hackertarget.com/reverseiplookup/?q="+target).text
      for i in r.split():
          print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] "+i)
      open(target+".txt", "w").write(r)
      print("\n"+Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+u"] Sonuçlar "+target+".txt'ye kaydedildi!")
      
def portscan():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
      print("")
      r = requests.get("https://api.hackertarget.com/nmap/?q="+target).text
      print(r)

def httpheader():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
      print("")
      r = requests.get("https://api.hackertarget.com/httpheaders/?q="+target).text
      print(r)

def whois():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
      print("")
      r = requests.get("https://api.hackertarget.com/whois/?q="+target).text
      print(r)
   
def geoiplookup():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Ip : ")
      print("")
      r = requests.get("https://api.hackertarget.com/geoip/?q="+target).text
      print(r)
      
def dnslookup():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
     print("")
     r = requests.get("https://api.hackertarget.com/dnslookup/?q="+target).text
     print(r)
     
def findshareddns():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
     print("")
     r = requests.get("https://api.hackertarget.com/findshareddns/?q="+target).text
     print(r)

def robotstxt():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     print("")
     r = requests.get(target+"/robots.txt").text
     print(r)
     
def finder(path):
     try:
       r = requests.get(target+path)
       if r.status_code==200:
          if re.search("404", r.text) or re.search("Not Found", r.text):
             pass
          else:
             print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] "+target+path)
     except:
       pass
def adminpanelfinder():
     clear()
     global target
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     thread = int(input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Thread : "))
     print("")
     panel = open("list/panel.txt", "r").read().splitlines()
     p = ThreadPool(thread)
     p.map(finder, panel)
     
def bannergrabbing():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Ip/24 : ")
     print("")
     r = requests.get("https://api.hackertarget.com/bannerlookup/?q="+target).text
     r = r.replace("{","")
     r = r.replace('"','')
     r = r.replace(":","")
     r = r.replace("}","")
     print(r)
def pagelinks():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     print("")
     r = requests.get(target)
     links = re.findall('href="(.*?)"',r.text)
     for i in links:
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] "+i)
    
def websiteonof():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     print("") 
     try:
        r = requests.get(target)
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] ONLINE ")
     except:
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] OFFLINE")

def ipfind():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
     print("") 
     showip = socket.gethostbyname(target)
     print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Ip : "+str(showip))
def subscan():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
     print("") 
     r = requests.get("https://api.hackertarget.com/hostsearch/?q="+target).text
     print(r)
     
def zonetransfer():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain : ")
     print("") 
     r = requests.get("https://api.hackertarget.com/zonetransfer/?q="+target).text
     print(r)
     
def testping():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
     print("") 
     r = requests.get("https://api.hackertarget.com/nping/?q="+target).text
     print(r)
     
def reversedns():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
     print("") 
     r = requests.get("https://api.hackertarget.com/reversedns/?q="+target).text
     print(r)
     
def directoryfuzz():
     clear()
     global target
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     thread = int(input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Thread : "))
     print("")
     direc = open("list/big.txt", "r").read().splitlines()
     p = ThreadPool(thread)
     p.map(finder, direc)
     
def emailextractor():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Url : ")
     print("")
     try:
       r = requests.get(target).text
     except:
        pass
     mails = re.findall(r'[\w\.-]+@[\w\.-]+', r)
     for i in mails:
           print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] "+i)
def subnetlookup():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Ip/24 : ")
     print("") 
     r = requests.get("https://api.hackertarget.com/subnetcalc/?q="+target).text
     print(r)

def nslookup():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Domain/Ip : ")
     print("")
     os.system("nslookup "+target)
def wpuserenumerate():
     clear()
     target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
     print("")
     try:
       r = requests.get(target+"/wp-json/wp/v2/users/").json()
     except:
       pass
     for i in r:
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Id : "+str(i['id'])+" User : "+str(i['name'])+" Username : "+str(i['slug']))
     
def alexacheck():
        clear()
        target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
        print("")
        r = requests.get("http://data.alexa.com/data?cli=10&dat=snbamz&url="+target)
        country = re.findall('" NAME="(.*?)"',r.text)
        globalrank = re.findall('" TEXT="(.*?)"',r.text)
        countryrank = re.findall('" RANK="(.*?)"', r.text)
        
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Country : " +str(country[0]))
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Global Rank : " +str(globalrank[0]))
        print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Country Rank : " +str(countryrank[0]))
     
def cloudflaredetect():
      clear()
      target = input(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] Site : ")
      print("")
      try:
        r = requests.get(target)
        if r.headers['Server'] == "cloudflare":
            print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+"] CloudFlare bulundu!")
        else:
            print(Fore.WHITE+"["+Fore.RED+"#"+Fore.WHITE+u"] CloudFlare bulunamadı!")
      except:
        pass