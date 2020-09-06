# minux on `feiniao`

`feiniao` (肥鸟 or 'fat bird' in chinese) is the name of my laptop and this 
repository gathers all the documentation and scripts to install and fine tune
ubuntu.

## Debiand unstable (10 / sid) on Dell XPS 13 2019

### Introduction

After one year running ubuntu 18.04, and a failed attempt to resize my swap
lvm volume leading to a kind of bricked system, I decided to make a fresh
debian install.

### Install process

#### References

I use the following web site to guide the main steps (Thanks Cedric Dufour).
http://cedric.dufour.name/blah/IT/DellXps9380DebianBuster.html

#### Downloading the iso

I am using [this iso](https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/daily-builds/sid_d-i/current/amd64/iso-cd/) for the unstable including non-free drivers.

#### Some notes for install

The install process is pretty straigthforward, go to expert mode, activate wifi
 with non free drivers. I used a lvm partition with three logical volumes 
for "/" "/home" and "/swap". I use 16G of swap even if the laptop has plenty
of RAM is some data science process, I need swap.

I choose also the kernel modules adapted to the configuraiton to have a slick
system. I might pay this back later when plugin some exotic hardware. Wait 
and see.

I don't install gnome, and just choose xcfe + debian graphical interfce.
Don't forget to add your user to the list of sudoers.

**Note on swap** : In previous install I had issues with system freeze while
 swaping, it seems to work perfectly now, in case of doubt you can perform 
stress tests on your machine, monitoring with htop

```
sudo apt install htop stress-ng
stress-ng --vm 2 --vm-bytes 1G --timeout 60s
```

You can increase the vm-byte step by step and check how swapping behaves.

More information there :
https://www.cyberciti.biz/faq/stress-test-linux-unix-server-with-stress-ng/

### Post install process

Following the boot, I follow the reference give above to fix few point
regarding configuration of hardware and high DPi screen.

#### HiDPI configuration

**GRUB**

Update `/etc/default/grub` with

```
GRUB_GFXMODE="1280x1024x32"
GRUB_GFXPAYLOAD_LINUX="keep"
GRUB_TERMINAL="gfxterm"
GRUB_CMDLINE_LINUX="video=1920x1080"
```

And then `sudo update-grub`

**LightDM greeter**

This section of the reference above is not really working, to be fixed later.
We will have a very small lightdm greeter.

**XFCE desktop**

Configure fonts scaling in XFCE Menu / Settings / Apprearance / Fonts / DPI
as 160.

#### Hardware support

Using the non-free installer, there is no need to install more packages for
hardware support, they are just listed here for reference.

```
firmware-misc-nonfree
xserver-xorg-video-intel
i965-va-driver
libvdpau-va-gl1
firmware-atheros
server-xorg-input-synaptics
```

**PS/2 Mouse**

We have to blacklist the mouse.

First edit this file :

```
# /etc/modprobe.d/psmouse-disable.conf
blacklist psmouse
```

and

```
update-initramfs -u
``` 

### Additionnal packages

```
sudo apt install snapd
snap install authy --beta
```

The path for snap is not update, for this I use a `.bash_profile` file which I source
when needed

```
export PATH="$PATH:/snap/bin"
``` 

### ssh configuration

Copy back your keys and install these in ~/.ssh with 600 permission mode.
Then you need to add your keys to your ssh-agent by doing `ssh-add ~/.ssh/id_rsa` if
standard key.


### Updating to SID / Unstable

The basic install was done using the testing debian stream, to switch to unsable / sid
you just have to update source.list and change buster to unstable and comment security
updates (which are done directly by packages maintainer in sid environement).

```
# testing
deb http://deb.debian.org/debian/ testing main contrib non-free
# dépôt sécurity testing 
deb http://deb.debian.org/debian-security/ testing-security/updates main contrib non-free
# unstable
deb http://deb.debian.org/debian/ unstable main contrib non-free
```
More information here :
https://debian-facile.org/doc:systeme:apt:sources.list:testing


### Power Management

Debian sid is handling power management on my machine much better than ubuntu. I 
don't know yet the reason but powertops is working well and I have now issue.

The only change that I made is concerning the suspend mode, I prefer to use
deep sleep than s2idle.

```
cat /sys/power/mem_sleep
```
showed
```
[s2idle] deep
```
As a temporary fix, I typed
```
echo deep > /sys/power/mem_sleep
```
as a root user (sudo -i).
Then the output of 
```
cat /sys/power/mem_sleep was
s2idle [deep]
```
After suspending now,
```
sudo journalctl | grep "PM: suspend" | tail -2 returns
PM: suspend entry (deep)
PM: suspend exit
```
I have made this permanent by editing
```
sudo vim /etc/default/grub
```
and replacing
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet"
```
with
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet mem_sleep_default=deep"
```
then regenerating my grub configuration :
```
update-grub
```
This appears to be working with no ill effects.

### Install R & Rstudio

There is a good guide available :
https://cran.rstudio.com/bin/linux/debian/#debian-sid-unstable

Install R-base system (it will be version 4.x as we are on unstable


Then for Rstudio, let's use the preview version (let's be crazy) to be 
installed with `gdebi`.

https://rstudio.com/products/rstudio/download/preview/

For Rstudio, you need to install ssh-askpass
```
sudo apt install ssh-askpass
```

### Communication tools

For Skype :

https://computingforgeeks.com/how-to-install-skype-on-debian/

```
wget https://go.skype.com/skypeforlinux-64.deb
sudo dpkg -i ./skypeforlinux-64.deb
```

This installation will add apt repository to /etc/apt/sources.list.d/skype-stable.list.


### Configure Chinese input

Configuration of chinese input is quite easy, there are just two
packages to install.

Check this wiki for reference : https://wiki.debian.org/InputMethodBuster
```
sudo apt install ibus ibus-libpinyin
ibus-daemon --xim -d
```
Then configure the input removing english and adding french & chinese.
This will run automatically after reboot


## Ubuntu configuration on Dell XPS 13 2019. 

Ubuntu is pre-installed on this Dell laptop, but their installation does not
include hard disk encryption. I attempted to use the recovery disk but failed to
install it again but it's buggy (hdd encryption password not recognized).

See this [post](https://www.dell.com/community/Linux-Developer-Systems/XPS-13-9370-Ubuntu-full-disk-encryption/td-p/6200577) for details.

So I decided to make a **fresh install** of ubuntu 18.04

__About the system__

`Linux feiniao 4.18.0-15-generic #16~18.04.1-Ubuntu SMP Thu Feb 7 14:06:04 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

## System configuration

In this part I come back on the essential points to configure or install the
base system.

### Touchpad

There is an issue with the standard installation and configuration of the 
touchpad which leads in jumping cursors. There could be a confusion by the 
daemon due to two touchpad detected. 

See Dell's fix to this issue.
https://www.dell.com/support/article/fr/fr/frbsdt1/sln308258/precision-xps-ubuntu-general-touchpad-mouse-issue-fix?lang=en

You have to edit this file

```
sudo vim /usr/share/X11/xorg.conf.d/51-synaptics-quirks.conf 
```

Add at the end :
```
Section "InputClass"
        Identifier "SynPS/2 Synaptics TouchPad"
        MatchProduct "SynPS/2 Synaptics TouchPad"
        MatchIsTouchpad "on"
        MatchOS "Linux"
        MatchDevicePath "/dev/input/event*"
        Option "Ignore" "on"
EndSection
```

This is supposed to work but I have still some issues and should look for a
reduction of the sensitivity of the device.

**Note**: Seems switching to Wayland ubuntu solves the problem.

### Vim

For most of my admin work and text edition I use Vim
```
sudo apt-get install vim
``` 

Vim is coming with plenty of packages, for autocompletion, terraform, etc...
The best is to set-up a package manager like ![vundle](https://github.com/VundleVim/Vundle.vim)

The install process is pretty straighforward.

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Then edit your .vimrc to use vundle, adding the configuration mentionned in the online
document.

And then to set-up a new plugin, like hashicorp terraform plugin, add the following to ~/.vimrc:
```
Plugin 'hashivim/vim-terraform'
```
Once this is done you can check which plugins are listed and install them.
from vim :

- `:PluginList` to check list of plugins
- `:PluginInstall` to install these
- ...

Other plugins :

- autocompletion : https://github.com/roxma/nvim-yarp (should need `pip3 install pynvimi`), https://github.com/ncm2/ncm2
- nvim-R : https://github.com/jalvesaq/Nvim-R https://github.com/gaalcaras/ncm-R




### Package management

To handle packages, I still find synaptic useful & apt-file to search
files in packages.

```
sudo apt-get install synaptic
sudo apt install apt-file
```

### Git

Git is a must !

```
sudo apt-get install git
```

### ssh & pgp keys

I am using ssh to commit on gitlab / github, i need to copy my private and 
public keys in `~/.ssh` and check they are chmod 600.

I use gnome-keyring to store all keys (ssh and pgp), `seahorse` is the program
to use for import & export. 
In order to add manually some password, the best is to use `secret-tool`.

```
sudo apt-get install libsecret-tools
```

### power management

It didn't work out of the box for me as the battery was drained quickly while on
suspend.

I tried first this approach :http://tipsonubuntu.com/2018/11/18/quick-tip-improve-battery-life-ubuntu-18-04-higher/

```
sudo apt install tlp
sudo add-apt-repository ppa:linuxuprising/apps
sudo apt install tlpui
```

Run by `pkexec /usr/sbin/lmt-config-gui`

Alternatively, there is another utility which seems to be better : `powertops`
https://wiki.archlinux.org/index.php/powertop


All of that didn't work very well, I finally found a bug from the previous
generation which seems still valid in the xps 13 9380. Basically, the laptop 
goes to sleep in sleep2idle instead of deep sleep. 

The fix is described here :
https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1808957

```
sudo journalctl | grep "PM: suspend" | tail -2.
```
If the output is
```
PM: suspend entry (s2idle)
PM: suspend exit
```
```
cat /sys/power/mem_sleep
```
showed
```
[s2idle] deep
```
As a temporary fix, I typed
```
echo deep > /sys/power/mem_sleep
```
as a root user (sudo -i).
Then the output of 
```
cat /sys/power/mem_sleep was
s2idle [deep]
```
After suspending now,
```
sudo journalctl | grep "PM: suspend" | tail -2 returns
PM: suspend entry (deep)
PM: suspend exit
```
I have made this permanent by editing
```
sudo vim /etc/default/grub
```
and replacing
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```
with
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash mem_sleep_default=deep"
```
then regenerating my grub configuration :
```
sudo grub-mkconfig -o /boot/grub/grub.cfg).
```
This appears to be working with no ill effects.


### Environement variables

I store some of the usefull code (API credentials for instance) as environment
variable.

You can edit  `.bash_profile` to store these :

```
export API_1="my cool code here"
export API_2="another_one"

```

If you are using travis for continuous integration with github, it's possible
then to encrypt you variable and add these to your project yaml file (see later)


## Web & password management

### `chromium-browser`

This tend to be my current browser with firefox install per default.
```
sudo apt-get install chromium-browser
```

### Dashlane

Then I install dashlane to get my password vault
https://www.dashlane.com/fr/download

I needed to install the windows client for some maintenance (there is only a
web client for linux)

***Install of wine***

Install Wine from Ubuntu repository
```
sudo apt install wine64
sudo apt-get remove winbind && sudo apt-get install winbind
sudo atp-get install winetricks
```
Launch winetricks to install vcrun2015 DLL.

Donwload the dashlane windows client and wine it from a terminal, this should work.

### Flash

Almost dead in 2019 but still some annoying websites uses it.
See : 
https://websiteforstudents.com/install-adobe-flash-player-on-ubuntu-18-04-lts-beta-desktop/

```
sudo add-apt-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"
sudo apt install adobe-flashplugin browser-plugin-freshplayer-pepperflash

```

### qBittorent


```
sudo apt-get install qBittorrent
```






## File Share, local & cloud

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


### Digital Ocean Spaces

Now that I have enough bandwidth, I store the data used in my dataprojects in 
a secure Digital Ocean Space.

> Digital Ocean spaces S3-compatible object storage with a built-in CDN that makes
 scaling easy, reliable, and affordable.

```
sudo apt install s3fs
mkdir ~/do
```

You should configure your .bash_profile with SPACE_KEY & SPACES_SECRET or
create a ~/.passwd-s3fs

```
echo $SPACES_KEY:$SPACES_SECRET > ~/.passwd-s3fs
chmod 600 ~/.passwd-s3fs
s3fs your-space /path/to/local/directory -ourl=https://nyc3.digitaloceanspaces.com -ouse_cache=/tmp
```



## Desktop

### XFCE

Add shortcut in preferences associated with this command

```
xfce4-session-logout --suspend
```

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

### Chinese

Just follow this guide :

https://www.pinyinjoe.com/linux/ubuntu-18-gnome-chinese-setup.htm


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
**Note:** this is not working so we have a TODO fix the config issues


### Digikam

We use also digikam to manage photo collection stored on NAS.
We use mysql (mariaDb).

```
sudo apt-get install digikam
sudo apt-get install libqt5sql5-mysql
```

When launching digikam need to use credential on the NAS, db names :

- digikam
- digikam-recognition
- digikam-thumbnails




## Editing

### `scribus`

To edit Photo Analogies magazine, we use both scribus stable and scribus-ng

```
sudo add-apt-repository ppa:scribus/ppa
sudo apt-get update
sudo apt-get install scribus
sudo apt-get install scribus-ng
```

Then you need to install color profiles for printing :

Download here :
http://www.eci.org/en/downloads
http://www.eci.org/_media/downloads/icc_profiles_from_eci/eci_offset_2009.zip

Add the profiles in your local config files :

https://wiki.scribus.net/canvas/Getting_and_installing_ICC_profiles

On Linux/Unix put your personal profiles into $HOME/.local/share/color/icc or $home/.color/icc (depending on the distribution and its version). System wide profiles for all users must be placed into /usr/share/color/icc.

### `pdftk`

I use pdftk to merge pdfs,

https://wilransz.com/pdftk-on-ubuntu-18-04/

```
sudo snap install pdftk
```


### `inkscape`

I use also inkscape for vector graphics

```
sudo apt-get install inkscape
```

### `Xournal`

Ligthweight note taking and pdf annotator. I install it from the Ubuntu software
center.



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

### Travis

I use travis for continuous integration with github and for blogdown / hugo 
websites. It's important to well configure the security for two aspects :

- encrypted System Environement variables
- keys for ssh deployment

#### Secure Environment variables

I followed this guide :
https://brettdewoody.com/secure-environment-variables-with-travis/


First, install the travis gem:

```
gem install travis
```

Then in your project directory run:

```
travis encrypt DB_URL=super_secret
```

This will return an encrypted string which can be added to the project's
.travis.yml file.

The .travis.yml file will now contain an entry of:

```
env:
  secure: MBxG/gsqeyONzA7wbWKACzv...
```


#### Secure deployment keys

TODO : write down the documentation here

### Postman

API development can be a nightmare if you cannot test easily, postman is the 
answer :

https://linuxize.com/post/how-to-install-postman-on-ubuntu-18-04/

```
sudo snap install postman
```


## e-mail

### Get packages 

Install necessary packages, for emailing we need, `mutt` as a client, 
`offlineimap` to get emails, `msmtp` to send emails (in fact `msmtp-gnome` 
pacakge to  get keyring support).  Email passwork will be stored in gnome 
keyring and we will use python keyring to access the keyring.

```
sudo apt-get install mutt offlineimap python-keyring msmtp msmtp-gnome
```

### Step one: `offlineimap`

Let's use the configuration file in the `mutt` subfolder of this repository
([`.offlineimaprc`](./mutt/.offlineimaprc)) . In addition, as usual archlinux is
the best documentation : 
https://wiki.archlinux.org/index.php/OfflineIMAP#Option_2:_gnome-keyring-query_script

### Step two: password & auth management

We will store the email password in seahorse which can be installed as package :

```
sudo apt install seahorse
```

The create an record for your passwordi with description = your_user@your_server.net.
We will use the 3rd option to manage passwords in offlineimaprc with a script 'gkgetsecret.py'

Store the script `gkgetsecret.py` available [here](https://github.com/charlesbos/my-scripts/blob/master/gkgetsecret.py).

Then in offlineimap change the two following parameters :

```
[Repository remote_main]

# to get the server fingerprint :
# openssl s_client -connect neomailbox.net:993 -servername neomailbox.net -showcerts < /dev/null 2>/dev/null   | openssl x509 -in /dev/stdin -sha1 -noout -fingerprint
#cert_fingerprint = <SHA1_of_server_certificate_here>
cert_fingerprint = 31:2C:....

remote_user = your_user
remotepasseval = get_pw_from_desc("your_user@your_server.net")


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

### zoom video conferencing

Download and install the latest package from Zoom
https://zoom.us/download


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


## Other

### Sonos
bof bof
https://www.ubuntupit.com/how-to-install-sonos-controller-app-noson-in-ubuntu/

bof
https://github.com/pascalopitz/unoffical-sonos-controller-for-linux/releases
sudo dpkg -i sonos-controller-unofficial-amd64.deb


### qgis
sudo apt-get install qgis


## Security

https://upcloud.com/community/tutorials/scan-ubuntu-server-malware/

### Evaluation

```
sudo apt-get install lynis
sudo lynis audit system
```

### Main changes

https://kifarunix.com/install-and-configure-aide-on-ubuntu-18-04/
```
sudo apt-get install aide
```
