# 💡 minecraft-light
A simple program to control smart bulb using Minecraft. I use this program for one of my video on Youtube.

# Dependencies
Hardware:
1. Yeelight Smart Bulb - Color W3
2. Smartphone (to connect smart bulb to Wi-Fi)

Software:
1. Minecraft server
2. Python 3
3. Python Library: ``mcpi``, ``yeelight``
4. Minecraft Plugin: ``Raspberry Juice``

# Installation
## Smart Bulb
Just follow the installation process through Yeelight app. Write down the IP of the smart bulb shown in the app.

## Python
```
pip install mcpi
pip install yeelight
```

## Minecraft
- Setup a minecraft server (I use Spigot version 1.16.5)
- Drag ``Raspberry Juice`` to plugin folder


# Setup
- Create a set of blocks with different color for trigger. Here I use ``redstone block`` for red, lapis ``lazuli block`` for blue, ``grass block`` for green, and ``sand block`` for yellow.
- Specify the smart bulb's IP in line 9 of ``main.py``
- Specify Minecraft server's IP and port in line 10 of ``main.py``
- Activate the program with ``python main.py``
- Program with brightness control can be used with ``python brightness.py``
- It should work
