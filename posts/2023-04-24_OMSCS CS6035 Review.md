---
title: OMSCS CS6035 Review
author: Kodama Chameleon
date: 2023-04-24
tags:
  - gatech
  - omscs
  - cybersecurity
---

![Gatech](/static/img/gatech_omscs.png)

Are you considering furthering your cyber career but unsure where to go or which courses to choose? The one who has ears, let them hear (proverbially speaking of course). A good friend and mentor of mine recommended the Georgia Institute of Technology’s online Master of Science in Cybersecurity (OMSCS), consistently rated as one of the top ten cybersecurity master’s programs in the country with an unbeatable tuition price tag. What chameleon could resist? Ok, but I am not here to sell you on a masters program. You are here to prepare for CS 6035, decide whether to take CS 6035, or perhaps just curious about my experiences this semester.

For the unenlightened, CS 6035 is the Introduction to Information Security course that all OMSCS students must take to graduate. The teaching staff generally recommend it as one of two courses to take first. The course consists of seven projects over two-week increments, with one extra credit opportunity. Say goodbye to boring papers, tests, quizzes… oops (here’s looking at you machine learning). Ok, so there was one little quiz, but more on that later. While various hyperlinks, videos, and other resource material is provided, be prepared to do much of your own research since this program is geared towards self-learners. Given that I, Kodama, fully support this type of self-exploration, there will be no spoilers here. Sorry, but not sorry! Most of the projects are integrated into autograder which (usually) provides instant feedback with (again, usually) “unlimited” number of submission attempts.

Our first project, Man in the Middle (someone make MITM more chameleon-sensitive, please), introduced the class to basic wireshark analysis. If you were hoping to capture the breeze between the trees, you’re out of luck. The pcap file was already provided, so you just have to chomp it up and digest it. Piece of grub if you have any networking experience, but still a great opportunity to better understand various protocols and some of the security concerns surrounding them.

From MITM, we moved on to Malware Analysis. Ctrl-F it already! ‘nuf said.

The “Web Security” project is the first in the series to require more coding, but don’t freak out! We’re talking very minimal coding at this point. Still, it pays to know a bit of PHP, SQL, and JavaScript beforehand. The teacher’s assistants (TAs) did an excellent job building you up to the three main tasks: cross-site request forgery (XSRF), cross-site scripting (XSS), and SQL injection.

Based on comments in ED discussions and Slack (the two approved means of class topic discussions), the next project is everyone’s favorite project to hate on, machine learning (ML). To be fair, ML happens to be one of the youngest members to join the CS 6035 course library, and this was its debut using the autograder functionality. The information security applications of machine learning, while totally relevant, got a little lost by many people due to the frustrating guessing games with the delivery medium, and yes, there was a little quiz thrown in there breaking the whole “no quizzes or test” vibe this course has going. Hopefully the TAs received some great feedback, and we look forward to hearing great things about this project in future iterations. Be prepared to use a lot of Python coding. Familiarity with Juypter notebooks is a plus!

![Grasping](/static/img/grasping_water.gif)

👆 Me trying to brute force the autograder during the machine learning project

Cryptography, although at times frustrating, was one of my favorite topics along with web security and binary exploitation. The main goal of the project was to create python code snippets that students could test in their local environment and, if done correctly, pass the autograder upon submission. This project is ideal for those who enjoy math as it involves converting mathematical algorithms to code in order to exploit cryptographic weaknesses.

Sandwiched between Cryptography and Binary Exploitation, the API security extra credit project boosted students’ grades while introducing key concepts such as JSON web tokens (JWT) and proper file permissions. Students who undertook the extra credit opportunity received a bit of a tail up on the last project over those who didn’t. The project also introduced useful tools such as Swagger and Postman.

If I asked you what coding language you might expect to demonstrate a buffer overflow, what would your answer be? If you said C or C++, then we have a winner! Not like C/C++ is the only language to have this problem, but it’s pretty infamous for it. In addition to C/C++, you will definitely need to know some python for the Binary Exploitation project. Some assembly knowledge wouldn’t hurt but is definitely not required. It also really pays to have a solid computer science foundation for this project since binary exploitation is really all about taking advantage of the underlying language all computers speak, 1’s and 0’s.

Our final project, Log4Shell, has to be one of the most infamous exploits of the past decade. Capturing the first couple of flags in this capture the flag (CTF) style project felt richly rewarding, and, son of a triceratops, that root shell felt so good! Unfortunately, the same reason that Log4Shell, [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) received a 10.0 in the National Vulnerability Database (NVD) may be the same reason our TA’s at Georgia Tech were left scrambling for more content to this project, it’s too freaking easy! After the first two flags, the rest start to feel a little contrived; fun little puzzles for a CTF game but not quite as likely to find in real world scenarious given the specificity of the code.

All-in-all this course delivered as promised an excellent introduction to information security. There’s no guarantee that future iterations will have the exact same projects or be in the same order; however, hopefully you found this write up useful as well as a little entertaining. If you liked this review and want to know when the next one will come out, here’s a hint: there are three semesters for this program and the spring semester is ending soon. Now go practice some good research habits and figure out when to expect my next course review! There’s no autograder for this task, but you do get “unlimited” attempts! 😝