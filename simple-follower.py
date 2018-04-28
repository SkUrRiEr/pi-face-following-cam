"""
Raspberry Pi + PanTiltHat face follower

Trivial face follower.

Copyright 2018 Julian Calaby

Run this script to do trivial face following with a pan tilt hat.
"""
import glob
import os
import sys
import select

import cv2

import config
import face

import pantilthat


if __name__ == '__main__':
	#pt = pantilthat.PanTiltHat()
	camera = config.get_camera()
	print('Trying to follow faces.')
	if config.DEBUG:
		print('Press q to quit.')
	else:
		print('Press Ctrl+C to quit.')

	#pt.pan(0)
	#pt.tilt(0)
	pan = 0
	tilt = 0

	pan_integral = 0
	tilt_integral = 0

	# Determine width and height
	image = camera.read()
	height, width, colours = image.shape

	while True:
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		image = camera.read()
		# Convert image to grayscale.
		image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

		if config.DEBUG:
			cv2.imshow('frame', image)

		# Get coordinates of single face in captured image.
		result = face.detect_single(image)
		if result is None:
			continue

		x, y, w, h = result

		print('Found face:', x, y, w, h)

		if config.DEBUG:
			cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)
			cv2.imshow('frame', image)

		# Centre of the face
		cx = x + w / 2
		cy = y + h / 2
		
		# Error
		ex = width / 2 - cx
		ey = height / 2 - cy

		print('error: ', ex, ey)

		pan = pan + ex / width
		tilt = tilt + ey / height

		if pan > 90:
			pan = 90
		elif pan < -90:
			pan = -90
		
		if tilt > 90:
			tilt = 90
		elif tilt < -90:
			tilt = 90
		
		print('Moving to: ', pan, tilt)

cv2.destroyAllWindows()
