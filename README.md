# Org-Doku

Take notes in Org-Mode and push them to any DokuWiki instance you control.

The initial goal of this project is to be able to take notes in Org-Mode and browse them in a familiar interface.

## Installation

This program needs Python 3, pip and pandoc installed on your machine in order to function properly.

```
git clone https://github.com/simsor/org-doku.git
cd org-doku
pip3 install -r requirements.txt
```

Create a file named `config.ini` in this directory and populate it with the URL, your username and password for the wiki.

```
url=https://wiki.oss.com
user=noel
password=hubertbonnisseurdelabath
namespace=rio
```

Org-Doku will manage the articles under the namespace you specify in the config file.

## Usage

`push.py` will look in the current directory for any Org files, convert them and push them to your wiki under the correct namespace.

`pull.py` will connect to your wiki and retrieve all the articles it can find that where written using this tool under a specific namespace.