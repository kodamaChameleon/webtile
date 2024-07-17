---
title: Call Me Gordon McPhish
author: Kodama Chameleon
date: 2023-09-27
tags:
  - cybersecurity
  - phishing
  - osint
---
Immersed in the academic bubble of Georgia Tech’s Master’s program, it’s pretty common to get a bit of a one-sided view of the real world. Exploring the world of machine learning for Intrusion Detection Systems (IDS) and how malware can outsmart these systems is downright intriguing. Yet, truth be told, your average cyber crook isn’t always the super-genius type or up for the hard work involved. They tend to go for the easier, lazy routes. That’s why it’s crucial to emphasize the fundamentals!

A friend of mine, knowing my cybersecurity background, sent me the following email they had received to investigate.

~~~
Hello, e****@gmail.com
Funds Are on the Way!

Pending eCheck payment confirmation

You have a pending eCheck payment from Gordon McCall (gm69camaro@gmail.com) for $425.00 USD.

-------------------------------------------------------------
Payment Details
-------------------------------------------------------------
Amount             $425.00 USD         
Transaction Date   October 29, 2023   
Transaction ID     6CX17026GD326612A   

To receive your payment, complete the one-page registration form [https://www.paypal.com/links/uni/em=e****@gmail.com&txn_id=5XY25873E58111219&unilat_id=6CX17026GD326612A&create_type=0?v=1&utm_source=unp&utm_medium=email&utm_campaign=RT000165&utm_unptid=97437736-767a-11ee-853d-3cfdfeef8069&ppid=RT000165&cnac=US&rsta=en_US%28en-US%29&cust=&unptid=97437736-767a-11ee-853d-3cfdfeef8069&calc=f71161276679e&unp_tpcid=email-unilateral-echeck-payment-notification-pending&page=main%3Aemail%3ART000165&pgrp=main%3Aemail&e=cl&mchn=em&s=ci&mail=sys&appVersion=1.211.0&xt=104038%2C124817].

Do not ship any items until you receive an email notification that the eCheck payment is complete, which usually takes 3-5 business days. You may withdraw your money at any time by requesting a check or by making a direct deposit to your bank account. You can also send the money to anyone with an email address.

You will be notified by email when your eCheck payment is complete. You can view the status of this payment at any time by logging in to your PayPal account.

Note: If you already have a PayPal account, be sure to add this email address to your account so you can receive your payment:

 1. Log in to your PayPal account [https://www.paypal.com/signin?v=1&utm_source=unp&utm_medium=email&utm_campaign=RT000165&utm_unptid=97437736-767a-11ee-853d-3cfdfeef8069&ppid=RT000165&cnac=US&rsta=en_US%28en-US%29&cust=&unptid=97437736-767a-11ee-853d-3cfdfeef8069&calc=f71161276679e&unp_tpcid=email-unilateral-echeck-payment-notification-pending&page=main%3Aemail%3ART000165&pgrp=main%3Aemail&e=cl&mchn=em&s=ci&mail=sys&appVersion=1.211.0&xt=104038%2C124817].
 2. Click the My Account tab.
 3. Select the Profile subtab.
 4. Add this email address to your PayPal account.

The payment will then be credited to your account.

Don't have a PayPal account?

Sign-up is fast and free. With PayPal, you can pay online without sharing your financial information.

You can also:

 * Send money to, or receive money from, anyone with an email address in the growing PayPal network.
 * Shop at millions of online stores

PayPal is the fast, easy and secure way to buy and sell things online.

PROTECT YOUR PASSWORD

NEVER give your password to anyone, including PayPal employees. Protect yourself against fraudulent websites by opening a new web browser (e.g. Internet Explorer or Firefox) and typing in the PayPal URL every time you log in to your account.

Not sure why you received this email? Learn more [https://www.paypal.com/us/smarthelp/article/why-am-i-receiving-emails-from-paypal-when-i-dont-have-an-account-faq4172?v=1&utm_source=unp&utm_medium=email&utm_campaign=RT000165&utm_unptid=97437736-767a-11ee-853d-3cfdfeef8069&ppid=RT000165&cnac=US&rsta=en_US%28en-US%29&cust=&unptid=97437736-767a-11ee-853d-3cfdfeef8069&calc=f71161276679e&unp_tpcid=email-unilateral-echeck-payment-notification-pending&page=main%3Aemail%3ART000165&pgrp=main%3Aemail&e=cl&mchn=em&s=ci&mail=sys&appVersion=1.211.0&xt=104038%2C124817]

 Copyright © 1999-2023 PayPal, Inc. All rights reserved. PayPal is located at 2211 N. First St., San Jose, CA 95131.

PayPal RT000165:en_US(en-US):1.0.0:f71161276679e
~~~

My friend, being the clever cookie she is, clocked this email for what it truly was: Gordon McCall? More like Gordon McPhish. This tech-savvy lizard dove straight into decrypting the lengthy hyperlinks for any signs of JavaScript trickery. But hold up! Surprisingly, there’s a much simpler attack hidden within this email. Can you spot it, though?!

The hard truth is that these mass campaigns don’t require genius tactics. They just need a handful of folks to take the bait. If you happened to spot the instructions suggesting adding gm69camaro@gmail.com to your PayPal account for that “payment” you’re expecting, congrats! You’ve dodged becoming a victim. But in case it’s not crystal clear, let me quickly break it down for you.

After you have followed Gordon’s instructions to add gm69camaro@gmail.com so you can get paid. Gordon attempts to log in to your account. Naturally, Gordon is a forgetful lad and “forgot” your password, so he takes advantage of PayPal’s forgot password feature to send a reset link to his email. Voila! Gordon now has full control of your PayPal account. The little snake!

![mcphish](/static/img/mcphish.png)

They say turning information into intelligence requires actionable steps, so let’s get to the “so what.” Firstly, avoid clicking on links from strangers. Nothing in this world truly comes for free. And certainly, steer clear of adding untrusted emails to your accounts, whether it’s PayPal or any other platform.

Moreover, enable multi-factor authentication (MFA) or two-factor authentication. Imagine if Gordon did manage to convince you to add his email to your account. Well, that MFA would surely throw a wrench in his plans when he attempts to log in with his snazzy new password but gets hit with a prompt for a PIN from a text or even better, a separate one-time password (OTP). Remember, when it comes to security, you want a layered defense.