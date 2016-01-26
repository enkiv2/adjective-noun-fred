#!/usr/bin/env python
import json
from random import Random
random = Random()

adjs=json.loads("\n".join(open("adjs.json").readlines()))["adjs"]
nouns=json.loads("\n".join(open("personal_nouns.json").readlines()))["personalNouns"]
nouns.extend(json.loads("\n".join(open("nouns.json").readlines()))["nouns"])
freds=json.loads("\n".join(open("firstNames.json").readlines()))["firstNames"]

print(" ".join([random.choice(adjs).capitalize(), random.choice(nouns).capitalize(), random.choice(freds)]))

