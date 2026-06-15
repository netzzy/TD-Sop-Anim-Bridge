"""Transcode a USD layer with usd-core.

Usage:
    python tools/transcode_usd.py input.usda output.usdc

The output file format is selected by its extension. This is intentionally
out-of-process from TouchDesigner so the TD process never imports pxr.
"""

import os
import sys

from pxr import Sdf


def transcode(src, dst):
	if not os.path.isfile(src):
		print('FAIL: input does not exist: %s' % src)
		return False

	layer = Sdf.Layer.FindOrOpen(src)
	if layer is None:
		print('FAIL: could not open input layer: %s' % src)
		return False

	folder = os.path.dirname(os.path.abspath(dst))
	if folder:
		os.makedirs(folder, exist_ok=True)

	if not layer.Export(dst):
		print('FAIL: could not export output layer: %s' % dst)
		return False

	check = Sdf.Layer.FindOrOpen(dst)
	if check is None:
		print('FAIL: output layer does not parse after export: %s' % dst)
		return False

	size = os.path.getsize(dst)
	print('PASS: wrote %s (%d bytes)' % (dst, size))
	return True


def main(argv):
	if len(argv) != 3:
		print('Usage: python tools/transcode_usd.py input.usda output.usdc')
		return 2
	return 0 if transcode(argv[1], argv[2]) else 1


if __name__ == '__main__':
	sys.exit(main(sys.argv))
