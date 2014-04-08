from jinja2 import Environment, FileSystemLoader

import json
import os
import sys

env = Environment(loader=FileSystemLoader("."))
template = env.get_template('ircd.conf.jinja')
motd = env.get_template('ircd.motd.jinja')

config = {}

with open(sys.argv[1] if len(sys.argv) > 1 else "config.json", "r") as fin:
    config = json.loads(fin.read())

network = config["network"]

for server in config["servers"]:
    with open("confs/" + server["name"]+".conf", "w") as fout:
        fout.write(template.render(**locals()))

    with open("confs/" + server["name"]+".motd", "w") as fout:
        fout.write(motd.render(**locals()))

