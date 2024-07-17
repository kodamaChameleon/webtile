---
title: Transforming with Holehe-Maltego
author: Kodama Chameleon
date: 2023-05-11
tags:
  - holehe
  - maltego
  - osint
---

![Holehe](/static/img/holehe.png)

Hello Maltego! A software that’s all about Transforms? Sounds like my kind of software. It’s free?! Could this get any… oh wait…

Ok, so join the club of hundreds if not thousands of software options with a free download and premium subscriptions. From video games to corporate level software solutions, it’s the same old bait and switch. No free lunch here, but just because many of the best options for Maltego require subscriptions doesn’t mean that there are some really great features in the community edition (CE). Thanks to the ability to add custom Transforms, Maltego has opened the door to tremendous opportunity for those willing to dig in a bit into the technical weeds.

Take Holehe-Maltego for example. I was first introduced to megadose’s GitHub library, [Holehe](https://github.com/megadose/holehe/),  shortly before my first Trace Labs capture the flag (CTF) search party. Holehe takes advantage of various password recovery, login, or register methods to identify if a specific email account is associated with a particular website. Sounds like a Maltego Transform in the making! Well the good news is megadose and his friend Mario Rojas (aka TURROKS) got you covered with [Holehe-Maltego](https://github.com/megadose/holehe-maltego). The one thing lacking (which I hope to remediate) is the lack of documentation for how a newbie such as myself goes about installing the Transform. The Wiki was quite lacking at the time of writing this article and various searches such as on YouTube were for an older version of holehe-maltego. If you find yourself in the same predicament, you’ve come to the right place.

Let’s start with some of the obvious, but sometimes overlooked, prerequisites. So you think you want to run a Maltego Transform? Maybe start by installing Maltego and signing in to your account. Sorry noobs, but I’m not going to hold your hand for this one. Maltego has good support documentation at [docs.maltego.com](https://docs.maltego.com/support/solutions/articles/15000008704-installing-maltego). In my case, utilizing the Trace Labs VM, Maltego is already installed as with most Kali and Parrot OS distributions.

The requirements.txt file list three additional python libraries: trio, holehe, and maltego-trx. The simplest solution is to use PyPI using the command:
```
pip install trio holehe maltego-trx
```
By default in the Trace Labs VM (which is really just a modified Kali Linux box), links to these python libraries will be installed at ~/.local/bin which is important to remember later in the process. The maltego-trx library is a more recent feature with holehe-maltego and is the reason older video tutorials were out of date with the current GitHub repo. There are a number of great features with maltego-trx which can be read about in more depth at [https://github.com/MaltegoTech/maltego-trx](https://github.com/MaltegoTech/maltego-trx). For our purposes, we just wanted to create a local Transform. To make the holehe-maltego library accessible to maltego-trx, simply ensure that you are in the same directory as maltego-trx and then clone the holehe-maltego git repository to that directory.

```
cd ~/.local/bin
git clone https://github.com/megadose/holehe-maltego.git
```
In Maltego, select the “New Local Transform” option from the top left corner. Enter the required details for step one. I used holehe for the display name and everything else the same as what is listed in the holehe-maltego transforms.csv file. Click next to continue to the command line options.

![holehe-maltego details](/static/img/holehe-maltego_details.png)

Under command, give the path to your python3.exe file. If python3 is already added to your PATH variable, this will just be python3. For the parameters enter “project.py local todetailsholehe.” For working directory, enter the fully qualified path to the holehe-maltego directory.

![holehe-maltego cmdLine](/static/img/holehe-maltego_cmdLine.png)

Hit finish and your done! You can now enjoy the power of holehe-maltego Transforms. Drag an email address entity from the entity palette; select the entity and enter the address you wish to investigate; right click and select run Transforms -> Local Transforms -> holehe. Finally, sit back and watch the magic happen.