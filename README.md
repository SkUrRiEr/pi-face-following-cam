Raspberry Pi Face Following Camera
==================================

Based on the Adafruit / Tony DiCola face recognition locked box project.


Dependencies
------------

The OpenCV bindings for Python 3 must be installed and must be version 2.4.9 or newer.

The data shipped with OpenCV must also be available. (This is the `opencv_data` package in Debian)

All other dependencies are managed using pipenv.

You _MUST_ enable site packages in pipenv by running `pipenv --site-packages` otherwise it won't be able to find `python-opencv`


Script Usage
------------

`main.py` is the main script, run this using pipenv to ensure that the dependencies are installed


References
----------

Adafruit / Tony DiCola face recognition locked box project:
 * https://github.com/tdicola/pi-facerec-box
 * http://learn.adafruit.com/raspberry-pi-face-recognition-treasure-box/overview
