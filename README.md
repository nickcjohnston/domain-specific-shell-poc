# domain-specific-shell-poc
Proof of concept ("PoC") for a generalized domain specific shell (similar to the Metasploit infosec tool). This PoC is a shell to help a dungeon master while building or running a gaming campaign.

This is super buggy and is only meant as a quick PoC.

## How to use
Add a class to the modules package. Just copy the base Module.py to get the scaffolding you need. The main program will use the *options* dictionary to get the module's options. Check out the Goblin.py example module. I'm going to add a settings file in the parent folder but for now, to change the greeting and default prompt just edit the dss.py file, you'll see globals at the top.

## Sample Run
<pre>
<span style="color:darkcyan;font-weight:bold;">$ tree | egrep -v '__'|pyc'; # Project Structure</span>
.
├── dss.py
└── modules
    ├── Goblin.py
    ├── Human.py
    ├── Illithid.py
    ├── Module.py

<span style="color:darkcyan;font-weight:bold;">$ ./dss.py</span>
Welcome to the rpg shell. Type a command after the <span style="color:darkcyan;font-weight:bold;">(rpg)</span> prompt to..do..stuff

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">help</span>
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

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">list</span>
Modules
-------
Human
Goblin
Illithid

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">use Goblin</span>
Using module Goblin

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">show</span>
Goblin
------
Generates goblins
----------
Options
-------
output_format = csv
quantity = 1

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">set quantity 5</span>

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">run</span>
Attack,Defense,Health
7,7,3
6,12,2
7,6,2
6,10,1
10,7,3

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">set output_format tsv</span>

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">run</span>
Attack	Defense	Health
8	8	2
6	9	4
7	6	2
7	8	3
7	5	1

<span style="color:darkcyan;font-weight:bold;">(Goblin)</span> <span style="font-weight:bold;">home</span>

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">2d5 </span>
Total	Rolls
3	2,1

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">4 2d5</span>
Totals	Rolls
6	3,3
2	1,1
5	1,4
4	1,3

<span style="color:darkcyan;font-weight:bold;">(rpg)</span> <span style="font-weight:bold;">quit</span>
</pre>
