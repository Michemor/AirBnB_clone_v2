#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static
using do_pack()
"""
from fabric.api import lcd, local, env
from datetime import datetime
from os.path import isdir, getsize


def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist)
    web_static_<year><month><day><hour><minute><second>.tgz
    returns the archive pack if generated correctky or else return None
    """
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + time_str + ".tgz"

    print(f"Packing web_static to {file_name}")
    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf %s web_static" % file_name).succeeded:
        print(f"web_static packed: {file_name} -> {getsize(file_name)}Bytes")
    else:
        return None
