
import dokuwiki

def get_config():
    result = {}
    with open("config.ini", "r") as f:
        for line in f:
            line = line.strip()
            key, value = line.split("=")

            result[key] = value

    return result


def connect_wiki(url, user, password):
    try:
        print("Trying to connect to DokuWiki...")
        wiki = dokuwiki.DokuWiki(url, user, password)
    except (dokuwiki.DokuWikiError, Exception) as err:
        print("Error connecting to DokuWiki: %s" % (err))

    return wiki
