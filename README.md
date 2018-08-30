# Bysykkel

Offers information of maximum available, and actual current available bicycles at each location in Oslo.

Installation on Ubuntu 16.04
--------------------------------------

sudo apt-get install python3-dev python3-pip

pip3 install --upgrade pip setuptools

cd ~

mkdir venvs

python3 -m venv venvs/flaskproj

source ~/venvs/flaskproj/bin/activate

mkdir ~/flaskproj

cd ~/flaskproj

pip install flask gunicorn

pip install requests

cd ~

gunicorn flaskproj:app

In browser: localhost:<portnumber from above e.g. 8000>

Todo
----
Format Web page	better,	improve	readability

Note
----
Change the api_token key in __init__.py file with your own! 
