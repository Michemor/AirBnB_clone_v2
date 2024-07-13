#!/usr/bin/env bash
# sets up web servers for deployment of web_static

if ! dpkg-query -s nginx > /dev/null 2>&1; then
    apt-get update
    apt-get install nginx -y
fi
service nginx start
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

echo " server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
    alias /data/web_static/current;
    index index.html index.htm;
    }
}" | tee /etc/nginx/sites-available/default > /dev/null
service nginx restart
