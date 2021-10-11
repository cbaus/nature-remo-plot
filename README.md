# Nature-remo-plot
This is a python project for plotting your temperature curves and other sensor information over time.
I wrote this for Nature Remo v3 but the API should be the same for the older models as well.

![Screenshot](https://github.com/cbaus/nature-remo-plot/raw/main/pics/remo-screenshot-1.png)

# Installation
  * Create a virtual environment for Python 3 ```python3 -m venv venv```
  * Install requirements ```pip install -r requirements.txt```
  * Set config: ```cp config.json.in config.json``` and add the token from https://home.nature.global/
# Usage
  * For data collection `./main.py`
  * For plotting `./plot.py`