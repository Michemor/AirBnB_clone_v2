#!/usr/bin/python3
"""
deploys the AirBnB clone from the local machine to the server
"""
from fabric.api import env, put, run, local
from os.path import exists, splitext, basename, isdir, getsize
from datetime import datetime

env.hosts = ["34.207.62.172", "35.175.128.130"]
env.user = "ubuntu"


def do_pack():
    """
    generated a .tgx archive
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


def do_deploy(archive_path):
    """
    do_deploy: deploys application to the server
    archive_path (str): path to the archived file
    """

    if exists(archive_path) is False:
        return False

    # web_file = .tgz
    web_file = basename(archive_path)

    # upload archive to directory
    if put(archive_path, "/tmp/{}".format(web_file)).failed is True:
        return False

    # create new path without .tzg extension
    filepath = splitext(web_file)[0]

    # create directory to which files will be uncompressed
    if run("mkdir -p /data/web_static/releases/{}/"
            .format(filepath)).failed is True:
        return False

    # uncompress files
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(web_file, filepath)).failed is True:
        return False

    # delete the archive
    if run("rm -rf /tmp/{}".format(web_file)).failed is True:
        return False

    # extract files from web_static and delete the web_static folder
    if run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"
            .format(filepath, filepath)).failed is True:
        return False

    # remove the web_static folder
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(filepath)).failed is True:
        return False

    # delete the link
    if run("rm /data/web_static/current").failed is True:
        return False

    # recreate the link
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filepath)).failed is True:
        return False

    print("New Version deployed!")
    return True


def deploy():
    """
    distributes an archive to your web servers
    """
    pack_return = do_pack()
    if pack_return:
        do_deploy(pack_return)
    return False
