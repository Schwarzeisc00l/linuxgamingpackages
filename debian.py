import os
import sys

print("Welcome to Schwarze's Package Installer Script.  It will install the packages for gaming. ")

if not os.geteuid() == 0:
    sys.exit("Please run the script as root or it might not work properly.\n")

update = input(("Would you like to update first? [1]Yes [0]No: "))
if  update == "1":
    os.system("sudo apt-get update && sudo apt-get upgrade")
    print("Done!")
else:
    print("Skipping!")


steam = input(("Would you like to install Steam for gaming? [1]Yes [0]No: "))
if steam == "1":
    os.system(" sudo apt-get install steam")
    print("Done!")
else:
    print("Skipping!")

lutris = input(("Would you like to install Lutris-an open source game launcher? [1]Yes [0]No: "))
if lutris == "1":
    os.system("sudo apt-get install lutris")
    print("Done!")
else:
    print("Skipping!")

playonlinux = input(("Would you like to install Playonlinux ? [1]Yes [0]No: "))
if playonlinux == "1":
    os.system("sudo apt-get install playonlinux")
else:
    print("Skipping!")

wine = input(("Would you like to install Wine compability tool? [1]Yes [0]No: "))
if wine == "1":
    os.system("sudo apt-get install wine")
    print("Done!")
else:
    print("Skipping!")

git = input(("Would you like to install git to clone? (Important) [1]Yes [0]No: "))
if git == "1":
    os.system("sudo apt-get install git")
    print("Done!")
else:
    print("Skipping!")

virtualbox = input(("Would you like to install Virtual Machine Manager for virtual machines? [1]Yes [0]No: "))
if virtualbox == "1":
    os.system("sudo apt-get install virt-manager")
    print("Done!")
else:
    print("Skipping!")

ufw = input(("Would you like to install Uncomplicated Firewall? [1]Yes [0]No: "))
if ufw == "1":
    os.system("sudo apt-get install ufw")
    print("Done!")
else:
    print("Skipping!")

minecraft = input(("Would you like to install Minecraft Launcher? [1]Yes [0]No: "))
if minecraft == "1":
    os.system("sudo apt-get install minecraft-launcher")
    print("Done!")

else:
    print("Skipping!")


flatpak = input(("Would you like to install flatpak ? [1]Yes [0]No: "))
if flatpak == "1":
    os.system("sudo apt-get install flatpak")
    print("Done!")
else:
    print("Skipping!")


spotify = input(("Would you like to install Spotify? [1]Yes [0]No: "))
if spotify == "1":
    os.system("sudo apt-get install spotify")
    print("Done!")
else:
    print("Skipping!")


discord = input(("Would you like to install Discord? [1] Yes [0]No "))
if discord == "1":
    os.system("sudo apt-get install discord")
    print("Done!")
else:
    print("Skipping!")
    
done = input(("That's it. Thanks for using my script. The source can be found on my Github page. Would you like to go now? [1]Yes [0]No: "))
if done == "1":
    os.system("firefox https://github.com/schwarzeisc00l")
    print("Done!")
else:
    print("Ok. Goodbye!")
