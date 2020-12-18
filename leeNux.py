from os import system
from time import sleep
from colorama import Fore, Back

system("clear")
print(Fore.WHITE+"", end="")
sleep(1.28)

system("sudo echo \"\"")
system("sudo clear")

print("LeeNux@boot~% start-boot[1] \n \n")
sleep(3)


print(Fore.WHITE+"")
system("sudo clear")
system("sudo apt update -y")
system("sudo clear")
system("sudo clear")
system("sudo apt install figlet -y")
system("sudo clear")
system("sudo apt install nano -y")
system("sudo clear")
system("sudo clear")
system("sudo pip install colorama")
system("sudo clear")
system("sudo apt install git -y")
system("sduo clear")
system("sudo /data/data/com.termux/files/usr/bin/python3 -m pip install --upgrade pip")
system("sudo clear")


print("\n LeeNux@boot~% boot-system[1] run!")
sleep(4)
system("clear")


def System():
    system("sudo clear")
    print(Fore.BLUE + "")
    system("sudo figlet LeeNux")
    print("------------"+Back.BLACK+Fore.WHITE+"NekClore"+Fore.BLUE+Back.RESET+"------------")

    print("\n \n \n \n")

    print(Fore.GREEN + "Enter \"l.help\", for help on the tool. \n \n")
    
    while True:
        
        os_set = input(Fore.RED + "[LeeNux@"+Fore.MAGENTA+"sec"+Fore.RED+"urity~$] " + Fore.YELLOW )
        print(Fore.YELLOW + "")
    
        if os_set == 'l.help':
            print("LeeNux - It is a tool for finding vulnerabilities in systems.")
            print("")
            print("l.(command) - In this format, the commands of this tool are indicated.")
            print("")
            print("This tool was created only for the sake of checking for security. If this tool is used not for good purposes, the developer is not responsible!")
            print("")
            print("Commands()")
            print("{")
            print("'help' - shows commands and useful text.")
            print("'install_(packet)' - loads the required tools / utilities / programs.")
            print("'begin_(script/program/utility)' - launching a script / program / utility.")
            print("'reboot' - reboots the system.")
            print("'update' - updates the system.")
            print("'hosts' - shows data about the saved user.")
            print("'hosts --add' - writes data about the user.")
            print("'hosts --rm' - removes all saved hosts.")
            print("'hosts --rw' - gives the user access to edit hosts.")
            print("'directory' - shows the directory where you are.")
            print("'openssh' - downloads and runs ssh.")
            print("'checkssh' - check ssh connection.")
            print("'killssh' - disconnect ssh connection.")
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
            print("}")
            
        elif os_set == "clear":
            System()
            
        elif os_set == "l.reboot":
            system("sudo python3 leeNux-termux.py")
            
        elif os_set == 'l.update':
            system("sudo apt update")
            system("sudo apt upgrade")
            
        elif os_set == 'l.hosts':
            system("sudo cat hosts.txt")
            
        elif os_set == 'l.hosts --add':
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
            system("sudo echo \"------------------------------------------------------------------------------\" >> hosts.txt")
            sleep(1)
            print("saving data ["+Back.YELLOW+"#"+Back.RESET+"   ] 25%")
            data_nhost1 = "IP: '"+ip_nhost+"' , ID: '"+id_nhost+"', Login: '"+login_nhost+"', Password: '"+password_nhost+"';"
            system("sudo echo \""+data_nhost1+"\" >> hosts.txt")
            sleep(1)
            print("saving data ["+Back.YELLOW+"##"+Back.RESET+"  ] 50%")
            data_nhost2 = "OS: '"+os_nhost+"', Ports: '"+ports_nhost+"', Location: '"+location_nhost+"';"
            system("sudo echo \""+data_nhost2+"\" >> hosts.txt")
            sleep(1)
            print("saving data ["+Back.YELLOW+"###"+Back.RESET+" ] 75%")
            data_nhost3 = "Name: '"+name_nhost+"', Second name: '"+secname_nhost+"', Nickname: '"+nickname_nhost+"', Birthday: '"+birthday_host+"';"
            system("sudo echo \""+data_nhost3+"\" >> hosts.txt")
            sleep(1)
            print("saving data ["+Back.YELLOW+"####"+Back.RESET+"] 100%")
            system("sudo echo \"------------------------------------------------------------------------------\" >> hosts.txt")
            system("sudo echo \"\" >> hosts.txt")
            system("sudo echo \"\" >> hosts.txt")
            sleep(2)
            print("\n host saved successfully!")
        elif os_set == 'l.hosts --rm':
            system("sudo rm hosts.txt")
            system("sudo >> hosts.txt")
            
        elif os_set == 'l.hosts --rw':
            system("sudo nano hosts.txt")
            
        elif os_set == 'l.directory':
            print("LeeNux$Directory")
            print("{")
            print(Fore.CYAN+"")
            system("pwd")
            print(Fore.YELLOW+"")
            print("}")
            
        elif os_set == 'l.openssh':
            system("sudo apt install openssh")
            system("sudo ssh-keygen")
            system("sudo cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys")
            system("sudo sshd")
            
        elif os_set  == 'l.install_metasploit':
            system("sudo apt install unstable-repo -y")
            system("sudo apt install metasploit -y")
            
        elif os_set == 'l.install_b0mb3r':
            system("sudo pip install b0mb3r")
            
        elif os_set == 'l.install_sqlmap':
            system("sudo apt install unstable-repo -y")
            system("sudo apt install sqlmap -y")
            
        elif os_set == 'l.install_nmap':
            system("sudo apt install nmap -y")
            
        elif os_set == 'l.install_PassGen':
            system("sudo git clone https://github.com/UnderMind0x41/PassGen")
            
        elif os_set == 'l.install_ssh':
            system("sudo apt install openssh -y")
            
        elif os_set == 'l.install_Fluxion':
            system("sudo git clone https://github.com/FluxionNetwork/fluxion")
            
        elif os_set == 'l.begin_metasploit':
            system("sudo msfconsole")
            
        else:
            system(os_set)

System()

