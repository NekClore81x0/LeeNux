from os import system
from time import sleep
from colorama import Fore
import subprocess

system("clear")
system("pkg update -y")
system("clear")
print("LeeNux@boot~% start-boot[1] \n \n")
print("|=================                                                                                   | 17%")
sleep(4)
system("clear")
system("pkg install figlet -y")
system("clear")
system("pkg install nano -y")
system("clear")
print("LeeNux@boot~% start-boot[1] \n \n")
print("|====================================                                                                | 36%")
sleep(4)
system("clear")
system("pip install colorama -y")
system("clear")
system("pkg install git -y")
system("clear")
print("LeeNux@boot~% start-boot[1] \n \n")

sleep(4)

print("\n LeeNux@boot~% boot-system[1] run!")
sleep(2)
system("clear")


def System():
    system("clear")
    print(Fore.BLUE + "")
    system("figlet LeeNux")

    print("\n \n \n \n")

    print(Fore.GREEN + "Enter \"lhelp\", for help on the tool. \n \n")
    
    while True:
        
        os_set = input(Fore.RED + "[LeeNux@"+Fore.MAGENTA+"sec"+Fore.RED+"urity~$] " + Fore.YELLOW )
        print(Fore.YELLOW + "")
    
        if os_set == 'lhelp':
            print("LeeNux - It is a tool for finding vulnerabilities in systems.")
            print("")
            print("leenux.(command) - In this format, the commands of this tool are indicated.")
            print("")
            print("This tool was created only for the sake of checking for security. If this tool is used not for good purposes, the developer is not responsible!")
            print("")
            print("Commands()")
            print("{")
            print("help - shows commands and useful text.")
            print("'install_(packet)' - loads the required tools / utilities / programs.")
            print("'reboot' - reboots the system.")
            print("'update' - updates the system.")
            print("'hosts' - shows data about the saved user.")
            print("'hosts --add' - writes data about the user.")
            print("'hosts --rm' - removes all saved hosts.")
            print("'hosts --rw' - gives the user access to edit hosts.")
            print("'directory' - shows the directory where you are.")
            print("'lopenssh' - downloads and runs ssh.")
            print("}")
            print("")
            print("Packets()")
            print("{")
            print("metasploit")
            print("b0mb3r")
            print("sqlmap")
            print("nmap")
            print("PassGen")
            print("ssh")
            print("Fluxion")
            print("php-apache")
            print("}")
            
        elif os_set == "clear":
            System()
            
        elif os_set == "lreboot":
            system("python3 LeeNux.py")
            
        elif os_set == 'lhosts':
            system("cat hosts.txt")
            
        elif os_set == 'lhosts --add':
            print("")
            ip_nhost = input("host IP>  ")
            id_nhost = input("host ID>  ")
            login_nhost = input("host login>  ")
            password_nhost = input("host password>  ")
            os_nhost = input("host OS>  ")
            ports_nhost = input("host ports>  ")
            location_nhost = input("host location>  ")
            name_nhost = input("host name>  ")
            secname_nhost = input("host second name>  ")
            nickname_nhost = input("host nickname>  ")
            birthday_host = input("host birthday>  ")
            print("")
            
            print("saving data [    ] 0%")
            system("echo \"------------------------------------------------------------------------------\" >> hosts.txt")
            sleep(1)
            print("saving data [#   ] 25%")
            data_nhost1 = "IP: '"+ip_nhost+"' , ID: '"+id_nhost+"', Login: '"+login_nhost+"', Password: '"+password_nhost+"';"
            system("echo \""+data_nhost1+"\" >> hosts.txt")
            sleep(1)
            print("saving data [##  ] 50%")
            data_nhost2 = "OS: '"+os_nhost+"', Ports: '"+ports_nhost+"', Location: '"+location_nhost+"';"
            system("echo \""+data_nhost2+"\" >> hosts.txt")
            sleep(1)
            print("saving data [### ] 75%")
            data_nhost3 = "Name: '"+name_nhost+"', Second name: '"+secname_nhost+"', Nickname: '"+nickname_nhost+"', Birthday: '"+birthday_host+"';"
            system("echo \""+data_nhost3+"\" >> hosts.txt")
            sleep(1)
            print("saving data [####] 100%")
            system("echo \"------------------------------------------------------------------------------\" >> hosts.txt")
            system("echo \"\" >> hosts.txt")
            system("echo \"\" >> hosts.txt")
            sleep(2)
            print("\n host saved successfully!")
        elif os_set == 'leenux.hosts --rm':
            system("rm hosts.txt")
            system(">> hosts.txt")
            
        elif os_set == 'lhosts --rw':
            system("nano hosts.txt")
            
        elif os_set == 'ldirectory':
            print("LeeNux$Directory")
            print("{")
            print(Fore.CYAN+"")
            system("pwd")
            print(Fore.YELLOW+"")
            print("}")
            
        elif os_set  == 'linstall_metasploit':
            system("pkg install unstable-repo -y")
            system("pkg install metasploit -y")
            
        elif os_set == 'linstall_b0mb3r':
            system("pip install b0mb3r")
            
        elif os_set == 'linstall_sqlmap':
            system("pkg install unstable-repo -y")
            system("pkg install sqlmap -y")
            
        elif os_set == 'linstall_nmap':
            system("pkg install nmap -y")
            
        elif os_set == 'linstall_PassGen':
            system("git clone https://github.com/UnderMind0x41/PassGen -y")
            
        elif os_set == 'linstall_ssh':
            system("pkg install openssh -y")
            
        elif os_set == 'linstall_Fluxion':
            system("git clone https://github.com/FluxionNetwork/fluxion -y")
            
        else:
            system(os_set)

System()
