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
Packages needed are : git python3

```
 git clone https://github.com/Schwarzeisc00l/linuxgamingpackages && cd linuxgamingpackages
 ```
Then you can do python3 archlinux.py to run.
This only supports Arch for now.
