---
title: Hunting the Cryptic Spectre
author: Kodama Chameleon
date: 2023-04-25
tags:
  - apt
  - malware
  - hacktoria
---

With the continual growth in capture the flag style events, Hacktoria recently launched the CTF Engineer Academy in order to recruit more like-minded individuals to meet the demand. On 24 April 2023, we welcomed the first contract created by the newly minted title, Hacktoria CTF Engineer. If you are looking for a nice little Cyber Threat Intelligence (CTI) teaser to flex some muscle on, Cryptic Spectre should be easy pickings for you.

We are provided with a malware hash and asked to determine the advanced persistent threat (APT) group and their target. For identification of malware, I quickly turned to one well known resource, [Virus Total](https://www.virustotal.com/). Virus Total’s public facing interface allows for the analysis of suspicious files, urls, domains, or hashes. Just be aware that uploading files does constitute sharing of said information with the security community, so don’t be uploading confidential or proprietary information.

If the results on the hash from Virus Total don’t bring out your inner deimatic display, I don’t know what will. Of 69 security vendors, 56 flagged the file as malicious, but we already knew that of course. What we care about in this scenario are the details and community tabs. Our malware hash resolves to the XTunnel implant associated with APT 28 (aka Fancy Bear or Sofacy). The top hit for a quick google search on the target of XTunnel sends us to an article by securityweek.com indicating the Democrat National Committee (DNC) as the target back in the summer of 2015.

Armed with the APT number and target, we now have all we need to complete the contract. My thanks to @LeRoux for contributing to the Hacktoria community with new contracts, and happy hunting to all!

![Cryptic Spectre](/static/img/ContractCard_CrypticSpectre.png)