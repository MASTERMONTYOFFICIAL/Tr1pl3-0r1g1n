<div align="center">

☠️ Tr1pl3-0r1g1n ☠️

Origin IP Discovery Tool

<!-- ASCII ART BANNER -->

<pre>
<span style="color: #FFD700;">
___________      ____       .__  ________           _______        ____       ____        
\__    ___/_____/_   |_____ |  | \_____  \          \   _  \______/_   | ____/_   | ____  
  |    |  \_  __ \   \____ \|  |   _(__  <   ______ /  /_\  \_  __ \   |/ ___\|   |/    \ 
  |    |   |  | \/   |  |_> >  |__/       \ /_____/ \  \_/   \  | \/   / /_/  >   |   |  \
  |____|   |__|  |___|   __/|____/______  /          \_____  /__|  |___\___  /|___|___|  /
                     |__|               \/                 \/         /_____/          \/ 
    Created by: Zer0pwn
</span>
</pre>

<p align="center">
<i>"Find Origin IP behind subdomain via AAA record !!"</i>
</p>

</div>

⚡ Description

Tr1pl3-0r1g1n is a Python tool developed by Zer0pwn. It automates the process of finding the origin IP address behind subdomains. It accepts a list of subdomains, cleans the input (removing http/https), and resolves the records to a file.

🛠️ Installation

You need Python 3 and the dnspython library.

Install the required library
```bash
pip3 install dnspython
```

```bash
git clone https://github.com/MASTERMONTYOFFICIAL/Tr1pl3-0r1g1n.git
python3 script.py
```

💻 Usage

Run the script using Python 3. You must provide a list of subdomains.

```bash
python3 script.py -l <list_of_subdomains.txt> [-o <output_file>]
```
Example Command:

```bash
python3 script.py -l list.txt -o results.txt
```
👤 Author

Name: Zer0pwn

⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only. The author is not responsible for any misuse.
