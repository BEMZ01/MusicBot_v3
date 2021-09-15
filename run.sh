#!/bin/sh
java -jar JAVA/jdk-13.0.2/bin/Lavalink.jar &
pip install discord.py[voice]
pip install wavelink
python launcher.py
