# linuxgamingpackages
A Python script that installs the important packages for you to game on linux properly.

# Enabling multilib
Multilib is generally used to run 32-bit applications on a 64-bit system. This is often useful when running older games or really anything else that is meant for 32-bit systems. Enabling support for multilib is a relatively common operation for many Arch Linux users. It is also relatively easy as far as Arch goes.


Open ```/etc/pacman.conf``` using your favourite editor and uncomment the following lines:
 ```
 [multilib]
 Include = /etc/pacman.d/mirrorlist
 ```
Then do a ```sudo pacman -Syyu```

# Installation
Packages needed are : git python3 python-pip



## Updated Best way to do it
```
 git clone https://github.com/Schwarzeisc00l/linuxgamingpackages && cd linuxgamingpackages
 ```
 and then python3 lgp.py to run. It detects the distro by itself. If you think some packages are missing or want support for another distro, or just found a bug, feel free to contact me.


## Arch Linux (Legacy)
```
 git clone https://github.com/Schwarzeisc00l/linuxgamingpackages && cd linuxgamingpackages
 ```
Then you can do python3 archlinux.py to run.
## Debian, Ubuntu (Legacy)
```
 git clone https://github.com/Schwarzeisc00l/linuxgamingpackages && cd linuxgamingpackages
```
Then you can do python3 debian.py to run.



# Changelog:
```
Added Discord
Added multilib support
Fixed some misspellings.
Fixed yay on Arch.
Added multi-distro support.






```

# Notes:
Please run the script as root. If you don't know what it means or how to do it,

```
sudo su
```
Now you are root.
