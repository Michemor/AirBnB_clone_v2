#!/usr/bin/env bash
# sets up web servers for deployment of web_static 

# checks whether nginx is installed, if not it installs it
apt update
apt install nginx -y

# create the following folders if they don't exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# create a fake html file
printf %s "
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html

# check for symbolic link and recreate it
ln -sf /data/web_static/releases/test/ /data/web_static/current

# grants ownership to group and user
chown -RL ubuntu:ubuntu /data/


# update nginx to serve content for hbnb_static
printf %s " server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
