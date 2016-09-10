#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import re

from common import get_config, connect_wiki


def convert_file(filename):
    name, ext = os.path.splitext(filename)
    if ext != ".org":
        return

    with open(filename, "r") as f:
        contents = f.read()

    regex = r"\$[^ ].+[^ ]\$"
    matches = re.findall(regex, contents)

    for i in range(0, len(matches)):
        match = matches[i]
        contents = contents.replace(match, "@@MATHJAX" + str(i) + "@@")
          
    sub = subprocess.run(["pandoc", "-f", "org", "-t", "dokuwiki"], stdout=subprocess.PIPE, input=contents, universal_newlines=True)
    out = sub.stdout
    
    for i in range(0, len(matches)):
        match = matches[i]
        out = out.replace("@@MATHJAX" + str(i) + "@@", match)
    
    print("File " + name + " converted to DokuWiki")
    return name, out

def get_mtime(f):
    stats = os.stat(f)
    return int(stats.st_mtime)

def get_last_modified():
    if not os.path.exists("last_modified"):
        open("last_modified", "w").write("0")
    
    with open("last_modified", "r") as f:
        return int(f.read())

def set_last_modified(n):
    with open("last_modified", "w") as f:
        f.write(str(n))

if __name__ == "__main__":
    config = get_config()
    wiki = connect_wiki(config["url"], config["user"], config["password"])
    
    files = os.listdir()
    last_modified = get_last_modified()
    new_last_modified = 0
    for f in files:
        mtime = get_mtime(f)
        if mtime < last_modified:
            # Then the file wasn't changed since the last push
            continue
        else:
            new_last_modified = max(new_last_modified, mtime)
        
        result = convert_file(f)
        if not result:
            continue
        
        name, contents = result
        with open(f) as orgfile:
            org = orgfile.read()

        if not name or not contents:
            continue
        
        wiki.pages.set(config["namespace"] + ":" + name, contents)
        wiki.pages.set(config["namespace"] + ":" + name + "_source", org)
        print("Pushed " + config["namespace"] + ":" + name)

    if new_last_modified:
        set_last_modified(new_last_modified)
