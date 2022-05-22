from email.message import Message
import json
import math
import sys
import os
from time import time, time_ns

MS_FILETIME_EPOCH = 116444736000000000

layout = {'content': []}

for (dirpath, dirnames, filenames) in os.walk("il-86"):
    for file in filenames:
        rel_dir = os.path.relpath(dirpath, "il-86")
        rel_file = os.path.join(rel_dir, file)
        rel_fix = rel_file.replace(".\\", "").replace("\\", "/")
        stat = os.stat(os.path.join(dirpath, file))
        layout["content"].append({'path': rel_fix, 'size': stat.st_size, 'date': int(
            stat.st_mtime_ns/100 + MS_FILETIME_EPOCH)})

layout["content"].insert(0, {'path': 'layout.json', 'size': 0, 'date': int(
    time_ns()/100 + MS_FILETIME_EPOCH)})


l = len(json.dumps(layout, indent=4, sort_keys=False))
while l != layout["content"][0]["size"]:
    layout["content"][0]["size"] = l
    layout["content"][0]["date"] = int(time_ns()/100 + MS_FILETIME_EPOCH)
    l = len(json.dumps(layout, indent=4, sort_keys=False))


with open('il-86/layout.json', 'w') as f:
    f.write(json.dumps(layout, indent=4, sort_keys=False))