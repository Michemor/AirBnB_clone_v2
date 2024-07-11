#!/usr/bin/env bash
# sets up web servers for deployment of web_static 

# checks whether nginx is installed, if not it installs it
if ! dpkg-query -s nginx &>/dev/null; then
    sudo apt update
    sudo apt install nginx -y
    sudo service nginx start
else
    echo "Nginx already installed"
fi

# create the following folders if they don't exist
folders=("/data/"
        "/data/web_static/"
        "/data/web_static/releases/"
        "/data/web_static/shared/"
        "/data/web_static/releases/test/")

# iterate through the folders, creating them if it doesn't exist
for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ] 
    then
        sudo mkdir "$folder"
    else
        echo "Directory $folder exists"
    fi
done

# create a fake html file
sudo touch /data/web_static/releases/test/index.html
sudo bash -c 'cat > '"/data/web_static/releases/test/index.html"' <<EOF
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
EOF'

# check for symbolic link and recreate it
sudo ln -sf  "/data/web_static/releases/test" "/data/web_static/current"
echo "symbolic link created"

# grants ownership to group and user
sudo chown -RL ubuntu:ubuntu "/data/"
echo "Successfully changed ownership"

# update nginx to serve content for hbnb_static
sudo bash -c 'cat > '"/etc/nginx/sites-available/default"' <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By 437274-web-01;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static/index.html {
        autoindex on;
        alias /data/web_static/current/index.html;
    }
}
EOF'

sudo service nginx restart
