#!/usr/bin/env python3

from common import get_config, connect_wiki

if __name__ == "__main__":
    config = get_config()
    wiki = connect_wiki(config["url"], config["user"], config["password"])

    pages = wiki.pages.list(config["namespace"])

    for page in pages:
        if page["id"].endswith("_source"):
            nosource = page["id"][0:-7]
            nonamespace = nosource[len(config["namespace"])+1:]
            with open(nonamespace + ".org", "w") as f:
                f.write(wiki.pages.get(page["id"]))
                print("Got " + nosource)
