
import dokuwiki
import sys

def get_config():
    result = {}
    try:
        with open("config.ini", "r") as f:
            for line in f:
                line = line.strip()
                key, value = line.split("=")
                
                result[key] = value
    except FileNotFoundError:
        print("Config file doesn't exist. See README.md for how to create it.")
        sys.exit(1)
              
    return result


def connect_wiki(url, user, password):
    try:
        print("Trying to connect to DokuWiki...")
        wiki = dokuwiki.DokuWiki(url, user, password)
    except (dokuwiki.DokuWikiError, Exception) as err:
        print("Error connecting to DokuWiki: %s" % (err))
        sys.exit(1)

    return wiki
