---
title: Made For Maltego
author: Kodama Chameleon
date: 2023-09-27
tags:
  - cti
  - maltego
  - osint
---

![MadeForMaltego](/static/img/firefly_nodes.png)

When I first got to know Maltego, it was like love at first sight for this chameleon! It felt as if Transforms were whispering my name. We were a match made in data heaven. But just like any relationship, that initial infatuation needs to grow into something more substantial if it's going to last. So, let's dive into Maltego as a powerful intelligence tool, shall we?

Before we take the plunge into the nitty-gritty, let's lay down a bit of groundwork regarding the intelligence lifecycle which can be broken down into 5 main phases. In phase 1 - "Planning and Direction" - the analyst receives directions from the customer in order to identify objectives, scope, and other requirements. Us internet sleuths love phase 2 - "Collection" - where we get to show off (or not) all our reconnaissance skills. For the data crunching nerds in phase 3 - "Analysis"- we break down all that gathered data into meaningful information which can lead to actionable intelligence. All of this work is meaningless though without phase 4 - "Production"- where the information actually gets packaged for phase 5 - "Dissemination and Feedback." Some organizations might have a slightly modified version of the intelligence life cycle, but the main building blocks are all the same.

![ThreatIntelLifeCycle](/static/img/The-Five-Stages-of-the-Cyber-Threat-Intelligence-Lifecycle.png)

So where does Maltego fit into the picture. As tempting as it is to view to see it as a collection tool, the brilliant mind behind the tool really meant it for analysis and production (see [Breadcrumbs: Episode 18. - Eat Your Own Dog Food - Talking Tools with Roelof Temmingh](https://podcasts.apple.com/us/podcast/breadcrumbs-by-trace-labs/id1542092539?i=1000558744203)). Maltego likes structured data. So, the notion of Maltego collecting DNS, WhoIs, emails, or a plethora of other data might seem like a bit of smoke and mirrors. In reality, this information has already been gathered, and whether it's residing on someone else's server or in a database is pretty much inconsequential. Indeed, the various Transform partners within Maltego can all be viewed as intelligence collection agencies. You're just paying for access to their preprocessed data for the purpose of analysis, production, and dissemination.

Naturally, there are exceptions to the rule. Some Transforms indeed adopt an active reconnaissance approach, but here's the catch – they often come with a side order of unpredictability. Small changes can render the entire process more broke then Twitter (ahem, X) when Elon decides to make it a paid service (shots fired).

![TongueShot](/static/img/tongueShot.gif)

What makes Maltego truly beautiful is its knack for unraveling the intricate web of relationships between entities. It's like a living tapestry, constantly weaving together ideas that evolve and expand as new datasets join the party. Now, that's a concept my chromatophores can rally behind any day!

*Side Note: If you love Maltego as much as I do and enjoy digging into open-source software, check out the local transforms at [MaltegoTech: Maltego-LTC](https://github.com/MaltegoTech/maltego-ltc).*