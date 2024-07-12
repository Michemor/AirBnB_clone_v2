#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static
# Checks if nginx is installed
sudo apt-get update
sudo apt-get install nginx -y

# Create the following folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a file with HTML content
sudo echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Checks for symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update file permissions
sudo chown -R ubuntu:ubuntu /data

# Update nginx to serve content for hbnb_static
sudo printf %s " server {
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

sudo service nginx restart
