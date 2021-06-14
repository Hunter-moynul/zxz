# Decompiled By Hunterboy Alamin
# NH KORSILAM ABLAMKI NH KORTE
# SURU KOSILA TOMRA  AKHON SHES AMI KORMO
#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m
TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB   
T:::::::::::::::::::::TH:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  
T:::::::::::::::::::::TH:::::::H     H:::::::H CC:::::::::::::::CB::::::BBBBBB:::::B 
T:::::TT:::::::TT:::::THH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::B     B:::::B
TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B
        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B
        T:::::T          H::::::HHHHH::::::HC:::::C                B::::BBBBBB:::::B 
        T:::::T          H:::::::::::::::::HC:::::C                B:::::::::::::BB  
        T:::::T          H:::::::::::::::::HC:::::C                B::::BBBBBB:::::B 
        T:::::T          H::::::HHHHH::::::HC:::::C                B::::B     B:::::B
        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B
        T:::::T          H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B
      TT:::::::TT      HH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::BBBBBB::::::B
      T:::::::::T      H:::::::H     H:::::::H CC:::::::::::::::CB:::::::::::::::::B 
      T:::::::::T      H:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  
      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB
                        

''')

print('''\033[91
                ``  ``...-...` ``                 
            ` `-+ssmdyshhyysdmdhs/.```            
          ``/oydy+:/m:+::+----yN+syyo:```         
        `.omMso::/+//////////odms+:/ydy/```       
      `.oydNNMo::````          `-oyhds+so:``      
    ` :ss+ymo:`.                   .+///+++- `    
   ``+syyy+.`  -.``           `...   `/oooo+: `   
  ``+ssss-.    ::-``.`      ``....`    -+o+++: `  
 ` :+sso..    `:-`.``        `  `-`     .++-:+- ` 
  .+:yo--     .:/``           ` -. `     -+:.//`  
` :++s+.      `-+`             `-.`.`     /-::-- `
` -o:s--     `./:`              -:..`     -/.--: `
``o-+s--     `-o.               ./-.      --:.:- `
` -++o:-      .o:` `:-`    .:. `:/-`      ---:.- `
` /-:oo``      -+:```     ````.::-`       ::..:- `
 `.+:o/:-      `.//. ``  ``:.-/-.`       --:-/: ``
 ` .:o-s-.      ``.:--``   -:..``       ././-.. . 
  ` :/:/:/-`     ```-/`   `:`          ----:/: `  
   ` .:++//:.`      `.:` `.`         .:::/:-. `   
    ` ./:-+://:.       ``        `-:--:.:::. `    
     ```-://:/+//-````     `   .-:/::+///:```     
       ```:////+/+yso+o/-:oosss/+o///+/. ``       
         ````.:+osyhdmssysyNmdhso/:-.```          
            ````.:+oyhy+oohddys+:-`               
                  `````....```       
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[93m
|****************************************************|
| Author   : Hunter-Moynul                          |
| Tool     : Termux All Package Install              |  
| Version  : 2.0                                     |
| Facebook : Termux help centre BD                  |
| Facebook ID : https://www.facebook.com/profile.php?id=100028650051426')
| Coded By : Dark Wolf , DarkXploit                  |
******************************************************''')

slowprint(''' \033[92m
 Package Name :

 openssh             wget
 clang               nmap
 python              python2
 python-dev          python3
 php                 nano
 java                git
 perl                bash
 curl                openssl
 w3m                 hydra
 ruby                macchanger
 host                dnsutils
 coreutils ''')
slowprint('''\033[92m
Termux Storage Permission''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [Yes/No] : ")
if choice == 'No' : sys.exit()
if choice == 'Yes' : os.system ("apt update")
os.system ("atp upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")
os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")
os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")

print ("Allow the Button For Access the Storage in Termux")


os.system ("termux-setup-storage")


