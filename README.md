# domain-specific-shell-poc
Proof of concept ("PoC") for a generalized domain specific shell (similar to the Metasploit infosec tool). This PoC is a shell to help a dungeon master while building or running a gaming campaign.

This is super buggy and is only meant as a quick PoC.

## How to use
Add a class to the modules package. Just copy the base Module.py to get the scaffolding you need. The main program will use the *options* dictionary to get the module's options. Check out the Goblin.py example module. I'm going to add a settings file in the parent folder but for now, to change the greeting and default prompt just edit the dss.py file, you'll see globals at the top.

## Sample Run
<pre>
<strong>$ tree | egrep -v '__'|pyc'; # Project Structure</strong>
.
├── dss.py
└── modules
    ├── Goblin.py
    ├── Human.py
    ├── Illithid.py
    ├── Module.py

<strong>$ ./dss.py</strong>
Welcome to the rpg shell. Type a command after the <span style="color:darkcyan;font-weight:bold;">(rpg)</span> prompt to..do..stuff

<strong>(rpg) help</strong>
Commands
--------
list
home
quit
exit
show
set
run
use
help

<strong>(rpg) list</strong>
Modules
-------
Human
Goblin
Illithid

<strong>(rpg) use Goblin</strong>
Using module Goblin

<strong>(Goblin) show</strong>
Goblin
------
Generates goblins
----------
Options
-------
output_format = csv
quantity = 1

<strong>(Goblin) set quantity 5</strong>

<strong>(Goblin) run</strong>
Attack,Defense,Health
7,7,3
6,12,2
7,6,2
6,10,1
10,7,3

<strong>(Goblin) set output_format tsv</strong>

<strong>(Goblin) run</strong>
Attack	Defense	Health
8	8	2
6	9	4
7	6	2
7	8	3
7	5	1

<strong>(Goblin) home</strong>

<strong>(rpg) 2d5 </strong>
Total	Rolls
3	2,1

<strong>(rpg) 4 2d5</strong>
Totals	Rolls
6	3,3
2	1,1
5	1,4
4	1,3

<strong>(rpg) quit</strong>
</pre>

## Sample Run 2

A different custom shell this time. Wrote a quick module to pull basic file stats for forensics

<pre>
<strong>$ ./dss.py</strong>
Welcome to the ftech shell. Type 'help' after the (ftech) prompt to see a list of commands

<strong>(ftech) help</strong>
Commands
--------
list
home
quit
exit
show
set
run
use
help

<strong>(ftech) list</strong>
Modules
-------
FileAnalysis

<strong>(ftech) use FileAnalysis</strong>
Using module FileAnalysis

<strong>(FileAnalysis) show</strong>
File Analysis
-------------
Generates basic metadata listings for files
----------
Options
-------
FILETYPE = True
HASH = sha512
STAT = True
FILEPATH = 

<strong>(FileAnalysis) set FILEPATH /home/nick/log.md</strong>

<strong>(FileAnalysis) show</strong>
File Analysis
-------------
Generates basic metadata listings for files
----------
Options
-------
FILETYPE = True
HASH = sha512
STAT = True
FILEPATH = /home/nick/log.md

<strong>(FileAnalysis) run</strong>
sha512 hash: cf42943423e0406c1d1c292075de62bace470e86b8aefd0e665dff4103ba94576b506e296f7dde8f8d02c6e46e380b10d58d80e3376226eaddba1d83e6f0fbed

File Type: ['UTF-8', 'Unicode', 'text']

Stat:   File: /home/nick/log.md
  Size: 2130      	Blocks: 8          IO Block: 4096   regular file
Device: 10301h/66305d	Inode: 6562341     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/    nick)   Gid: ( 1000/    nick)
Access: 2019-04-15 11:24:02.894180697 -0400
Modify: 2019-04-15 11:24:01.670154349 -0400
Change: 2019-04-15 11:24:01.678154521 -0400
 Birth: -

<strong>(FileAnalysis) home</strong>

<strong>(ftech) quit</strong>
</pre>
