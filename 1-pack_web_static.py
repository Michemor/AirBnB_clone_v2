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
    generates a .tgz archive from the contents of the web_static
    """
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + time_str + ".tgz"

    print(f"Packing web_static to {file_name}")
    if isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf %s web_static" % file_name).succeeded is True:
        print(f"web_static packed: {file_name} -> {getsize(file_name)}Bytes")
        return file_name
    else:
        return None
