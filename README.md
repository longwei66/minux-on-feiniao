# minux-on-feiniao

## Introduction
### Purpose of this Readme
This document is about Ubuntu configuration on Dell XPS 13 2019. 
Ubuntu is pre-installed on the laptop, but their installation does not include hard disk encryption and the recovery disk is buggy.
https://www.dell.com/community/Linux-Developer-Systems/XPS-13-9370-Ubuntu-full-disk-encryption/td-p/6200577

So I made a fresh install of ubuntu 18.04

### About the system
`Linux feiniao 4.18.0-15-generic #16~18.04.1-Ubuntu SMP Thu Feb 7 14:06:04 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

## What to configure after first login
The systems works off the shelve, basically I just had to install my favorite packages and tweak few stuffs.


## Additionnal software install

### Web & password management
Firs I install `chromium-browser` which tend to be my current browser.
Then I install dashlane to get my password vault
https://www.dashlane.com/fr/download

### System

#### Vim
For most of my admin work and text edition I use Vim
```
sudo apt-get install vim
``` 

#### Package management
To handle packages, I still find synaptic useful.
```
sudo apt-get install synaptic
```

#### Git
Git is a must !
```
sudo apt-get install git
```

#### ssh
I am using ssh to commit on gitlab / github, i need to copy my private and public keys in `~/.ssh`


#### shared folders
I use a NAS and basically need to mount the shared folders I use. I need here to modify `/etc/fstab`

First I need to create the directory structure 

```
sudo mkdir /media/lagrange
sudo chown longwei:longwei /media/lagrange/
cd /media/lagrange/
mkdir lagrange_photographie
mkdir lagrange_multimedia
mkdir lagrange_photos_videos
mkdir lagrange_atelier
mkdir homes
mkdir homes/lagrange_barthelemy
```

Then I need to install cifs utils to get the samba access.
```
sudo apt-get install cifs-utils
```

Then I need to create a protected file to store my samba password as root `sudo vim /etc/cifspwd`
```
username=<username on server>
password=<password for that username>
```
And then change the access rights.
```
sudo chmod 600 /etc/cifspwd
```

Bellow are the lines to add at the end of `/etc/fstab` file which should contain :

```
# NAS 
//192.168.2.108/photographie /media/lagrange/lagrange_photographie cifs user,uid=longwei,gid=users,rw,suid,credentials=/etc/cifspwd 0 0
//192.168.2.108/multimedia /media/lagrange/lagrange_multimedia cifs user,uid=longwei,gid=users,rw,suid,credentials=/etc/cifspwd 0 0
//192.168.2.108/photos_videos /media/lagrange/lagrange_photos_videos cifs user,uid=longwei,gid=users,rw,suid,credentials=/etc/cifspwd 0 0
//192.168.2.108/atelier /media/lagrange/lagrange_atelier cifs user,uid=longwei,gid=users,rw,suid,credentials=/etc/cifspwd 0 0
//192.168.2.108/homes/barthelemy /media/lagrange/homes/lagrange_barthelemy cifs user,uid=longwei,gid=users,rw,suid,credentials=/etc/cifspwd 0 0
```

#### nextcloud
I use nextcloud client to synchronise with my local cloud (NAS) and remote private cloud
https://launchpad.net/~nextcloud-devs/+archive/ubuntu/client
```
sudo add-apt-repository ppa:nextcloud-devs/client
sudo apt-get update
sudo apt-get install nextcloud-client
```

I configure my login and launch of the add at startup.
http://192.168.2.108/owncloud


### Desktop

#### gnome 3
I'd like to remove icons from the desktop, first install `sudo apt-get install dconf-editor`
Launch `dconf-editor` and Locate /org/gnome/desktop/background/ and untick the show desktop icons.

#### conky
```
sudo apt-get install conky-all
```

See `./conky` folder in this repo for conky configuration.



### Photo & multimedia
```
sudo apt-get install gimp
sudo apt-get install darktable
sudo apt-get install geeqie
sudo apt-get install vlc
```

For darktable, it's better to activate openCL capabilities :
```
sudo apt install ocl-icd-opencl-dev
``` 


### Editing
To edit Photo Analogies magazine, we use both scribus stable and scribus-ng
```
sudo add-apt-repository ppa:scribus/ppa
sudo apt-get update
sudo apt-get install scribus
sudo apt-get install scribus-ng
```
I use also inkscape for vector graphics
```
sudo apt-get install inkscape
```

### Coding

#### R

I follow this guide to install latest R packages
https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04
(step1)
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt update
sudo apt install r-base
```

#### Rstudio
Rstudio (preview version)
```
wget https://s3.amazonaws.com/rstudio-ide-build/desktop/trusty/amd64/rstudio-1.2.1280-amd64.deb
sudo apt-get install libclang-dev
sudo dpkg -i rstudio-1.2.1280-amd64.deb
```


### e-mail & communication

#### mutt & offlineimap
```
sudo apt-get install mutt offlineimap
```
Then for configuration follow the step bellow ...

#### irssi
```
sudo apt-get install irssi
```


#### signal

Install and add device

```
sudo apt-get install curl
curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -
echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list
sudo apt update && sudo apt install signal-desktop
```

