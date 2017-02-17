#!/bin/sh

path=${PWD##*/}
if [ "$path" = "AlertMe" ]
then
  echo "Trying to install required packages..."

  # Install required packages
  pip3 install python3-xlib
  sudo apt-get install scrot
  sudo apt-get install python3-tk
  sudo apt-get install python3-dev
  sudo apt-get install notify-osd
  pip3 install pyautogui

  # Set up files
  echo "Trying to add folder /etc/AlertMe..."
  sudo mkdir /etc/AlertMe
  {
    sudo cp ./__init__.py /etc/AlertMe
    sudo cp ./__main__.py /etc/AlertMe
    sudo cp ./watching.py /etc/AlertMe
    echo "Files copied..."
  } || {
    echo "Could not copy files to /etc/AlertMe..."
    echo "Try and do it manually..."
  }
  read -p "Do you want this script to start at boot? (y/n)" yn
  case $yn in
    [Yy]* ) echo "Copying boot file..."; sudo cp ./AlertMe.sh /etc/init.d/; sudo chmod +x /etc/init.d/AlertMe.sh; echo "Copied boot file...";;
    [Nn]* ) echo "OK. You can always add boot.sh later yourself..."; exit;;
    * )     echo "Please answer yes or no...";;
  esac
else
  echo "You have to be inside the AlertMe folder to execute this file..."
fi
