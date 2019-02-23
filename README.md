# minux-on-feiniao

## Introduction
### Purpose of this document is about Ubuntu configuration on Dell XPS 13 2019. 
Ubuntu is pre-installed on the laptop, but their installation does not include hard disk encryption and the recovery disk is buggy.
https://www.dell.com/community/Linux-Developer-Systems/XPS-13-9370-Ubuntu-full-disk-encryption/td-p/6200577

So I made a fresh install of ubuntu 18.04

### About the system
`Linux feiniao 4.18.0-15-generic #16~18.04.1-Ubuntu SMP Thu Feb 7 14:06:04 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

## Web & password management

### `chromium-browser`

This tend to be my current browser with firefox install per default.
```
sudo apt-get install chromium-browser
```

### Dashlane

Then I install dashlane to get my password vault
https://www.dashlane.com/fr/download

## System

### Vim
For most of my admin work and text edition I use Vim
```
sudo apt-get install vim
``` 

### Package management

To handle packages, I still find synaptic useful.
```
sudo apt-get install synaptic
```

### Git

Git is a must !
```
sudo apt-get install git
```

### ssh & pgp keys
I am using ssh to commit on gitlab / github, i need to copy my private and public keys in `~/.ssh`

I use gnome-keyring to store all keys (ssh and pgp), `seahorse` is the program
to use for import & export. 
In order to add manually some password, the best is to use `secret-tool`.
```
sudo apt-get install libsecret-tools
```

### power management

Not super convinced this is usefull !

```
sudo apt install laptop-mode-tools
```

Run by `pkexec /usr/sbin/lmt-config-gui`

## Local network

### shared folders
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

TODO : seems the partitions are not mounted automatically at reboot ???

### nextcloud
I use nextcloud client to synchronise with my local cloud (NAS) and remote private cloud
https://launchpad.net/~nextcloud-devs/+archive/ubuntu/client
```
sudo add-apt-repository ppa:nextcloud-devs/client
sudo apt-get update
sudo apt-get install nextcloud-client
```

I configure my login and launch of the add at startup.
http://192.168.2.108/owncloud


## Desktop

### gnome 3

I'd like to remove icons from the desktop, first install `sudo apt-get install dconf-editor`
Launch `dconf-editor` and Locate /org/gnome/desktop/background/ and untick the show desktop icons.

### conky
```
sudo apt-get install conky-all
```

See [./conky/.conkyrc](./conky/.conkyrc) in this repo for conky configuration.
Thanks : https://www.splitbrain.org/blog/2016-11/20-simple_conky_setup

Then add it to startup with `gnome-session-properties`

## Photo & multimedia

### Must have packages

```
sudo apt-get install gimp
sudo apt-get install darktable
sudo apt-get install geeqie
sudo apt-get install vlc
```

### Darktable extra config

For darktable, it's better to activate openCL capabilities :

```
sudo apt install ocl-icd-opencl-dev
``` 
TODO fix the config issues


## Editing

### `scribus`

To edit Photo Analogies magazine, we use both scribus stable and scribus-ng

```
sudo add-apt-repository ppa:scribus/ppa
sudo apt-get update
sudo apt-get install scribus
sudo apt-get install scribus-ng
```

### `inkscape`

I use also inkscape for vector graphics

```
sudo apt-get install inkscape
```

## Coding

### R

I follow this guide to install latest R packages
https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04
(step1)

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
sudo apt update
sudo apt install r-base
```

### Rstudio

Rstudio (preview version)
```
wget https://s3.amazonaws.com/rstudio-ide-build/desktop/trusty/amd64/rstudio-1.2.1280-amd64.deb
sudo apt-get install libclang-dev
sudo dpkg -i rstudio-1.2.1280-amd64.deb
```


## e-mail

### Get packages 

Install necessary packages, for emailing we need, `mutt` as a client, 
`offlineimap` to get emails, `msmtp` to send emails (in fact `msmtp-gnome` pacakge
to  get keyring support).  Email passwork will be stored in gnome keyring and we
will use python keyring to access the keyring.

```
sudo apt-get install mutt offlineimap python-keyring msmtp msmtp-gnome
```

### Step one: `offlineimap`

Let's use the configuration file in the `mutt` subfolder of this repository
(`.offlineimaprc` and `.offlineimap` dir) . In addition, as usual archlinux is
the best documentation : 
https://wiki.archlinux.org/index.php/OfflineIMAP#Option_2:_gnome-keyring-query_script

### Step two: password & auth management

We will store the email password in keyring, to add you email password in the keyring :

```
$ python2
>>> import is Readme
Thkeyring
>>> keyring.set_password("offlineimap","username@host.net", "MYPASSWORD")
```

### Step three: automation of get emails

We need to automate the offlineimap launch (TODO)

### Step four: send emails with `msmtp`

For email sending we use `msmtp`, a configuration file [`.msmtprc`](./mutt/.msmtprc) is also
available in the `mutt` subfolder of this repository. You need to make sure that
the smtp password of your email account is stored in you keyring.
```
secret-tool store --label=msmtp host xxx.net service smtp user yyyy
```


### Step five: `mutt` configuration

Finally we can configure `mutt`, you will find in the subfolder
both `.muttrc` file and `.mutt/` folder to install in your `home` folder. 

## messenging

### irssi
```
sudo apt-get install irssi
```


### signal

Install and add device

```
sudo apt-get install curl
curl -s https://updates.signal.org/desktop/apt/keys.asc | sudo apt-key add -
echo "deb [arch=amd64] https://updates.signal.org/desktop/apt xenial main" | sudo tee -a /etc/apt/sources.list.d/signal-xenial.list
sudo apt update && sudo apt install signal-desktop
```

## Virtualisation

### Virtualbox packages

I use virtualbox to virtualize machines (other linux distrib) or other OS for some
tests.

```
sudo apt-get install virtualbox
```

### Virtualbox extensions
