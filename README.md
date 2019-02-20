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

#### Package management
To handle packages, I still find synaptic useful.
`sudo apt-get install synaptic`

#### nextcloud
I use nextcloud client to synchronise with my local cloud (NAS) and remote private cloud
https://launchpad.net/~nextcloud-devs/+archive/ubuntu/client
`sudo add-apt-repository ppa:nextcloud-devs/client`
`sudo apt-get update`
`sudo apt-get install nextcloud-client`

I configure my login and launch of the add at startup.
http://192.168.2.108/owncloud

#### conky
`sudo apt-get install conky`

(see configuration bellow)

### Photo & multimedia
`
sudo apt-get install gimp
sudo apt-get install darktable
sudo apt-get install geeqie
sudo apt-get install vlc
`

### Editing
To edit Photo Analogies magazine, we use both scribus stable and scribus-ng
`
sudo add-apt-repository ppa:scribus/ppa
sudo apt-get update
sudo apt-get install scribus
sudo apt-get install scribus-ng
`
I use also inkscape for vector graphics
`
sudo apt-get install inkscape
`

### Coding

#### R

I follow this guide to install latest R packages
https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04
(step1)
`
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt update
sudo apt install r-base

`


R (complete with packages)
Rstudio (dev version)



### e-mail & communication
irssi
signal
mutt
imap ???




