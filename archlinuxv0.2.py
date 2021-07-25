import os
print("Welcome to Schwarze's Package Installer Script.  It will install the packages for gaming. ")
update = input(("Would you like to update first? [1]Yes [0]No: "))
if  update == "1":
    os.system("sudo pacman -Syu")
    print("Done!")
else:
    print("Skipping!")

yay = input(("Would you like to install YAY- Arch User Repository? [1]Yes [0]No: " ))
if yay == "1":
    os.system("sudo pacman -S git base-devel && cd /opt  && sudo git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si ")
    print("Done!")
else:
    print("Skipping!")

steam = input(("Would you like to install Steam for gaming? [1]Yes [0]No: "))
if steam == "1":
    os.system("sudo pacman -S steam")
    print("Done!")
else:
    print("Skipping!")

lutris = input(("Would you like to install Lutris-an open source game launcher? [1]Yes [0]No: "))
if lutris == "1":
    os.system("sudo pacman -S lutris")
    print("Done!")
else:
    print("Skipping!")

playonlinux = input(("Would you like to install Playonlinux ? [1]Yes [0]No: "))
if playonlinux == "1":
    os.system("sudo pacman -S playonlinux")
else:
    print("Skipping!")

wine = input(("Would you like to install Wine compability tool? [1]Yes [0]No: "))
if wine == "1":
    os.system("sudo pacman -S wine")
    print("Done!")
else:
    print("Skipping!")

git = input(("Would you like to install git to clone? (Important) [1]Yes [0]No: "))
if git == "1":
    os.system("sudo pacman -S git")
    print("Done!")
else:
    print("Skipping!")

virtualbox = input(("Would you like to install Virtualbox for virtual machines? [1]Yes [0]No: "))
if virtualbox == "1":
    os.system("sudo pacman -S virtualbox")
    print("Done!")
else:
    print("Skipping!")

ufw = input(("Would you like to install Uncomplicated Firewall? [1]Yes [0]No: "))
if ufw == "1":
    os.system("sudo pacman -S ufw")
    print("Done!")
else:
    print("Skipping!")

minecraft = input(("Would you like to install Minecraft Launcher? (Make sure you have yay installed)[1]Yes [0]No: "))
if minecraft == "1":
    os.system("yay  -S minecraft-launcher")
    print("Done!")

else:
    print("Skipping!")


flatpak = input(("Would you like to install flatpak ? [1]Yes [0]No: "))
if flatpak == "1":
    os.system("sudo pacman -S flatpak")
    print("Done!")
else:
    print("Skipping!")


spotify = input(("Would you like to install Spotify? [1]Yes [0]No: "))
if spotify == "1":
    os.system("sudo pacman -S spotify")
    print("Done!")
else:
    print("Skipping!")

optimusmanager =input(("Would you like to install Optimus Manager to switch between gpu's? [1]Yes [0]No: "))
if optimusmanager == "1":
    os.system("yay -S nvidia && yay -S base-devel &&  yay -S optimus-manager optimus-manager-qt && sudo systemctl enable optimus-manager ")
    print("Done!")
else:
    print("Skipping!")

done = input(("That's it. Thanks for using my script. The source can be found on my Github page. Would you like to go now? [1]Yes [0]No: "))
if done == "1":
    os.system("firefox https://github.com/schwarzeisc00l")
    print("Done!")
else:
    print("Ok. Goodbye!")
