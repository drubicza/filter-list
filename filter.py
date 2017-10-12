import argparse

halah = argparse.ArgumentParser(description="Filtering words tools by unique")
halah.add_argument("-i", type=str, action="store", help="Input file name")
halah.add_argument("-out", type=str, action="store", help="Output file name")

zeeb = halah.parse_args()

if zeeb.i and zeeb.out:
	f = open(zeeb.i, "r").read().split()
	w = open(zeeb.out, "w")
	wibu = {""}
	w.write("Filtered List, Tools can found in https://github.com/B3yeZ/")

	for yo in f:
		wibu.add(yo)
	for x in wibu:
		w.write(x + "\n")

	w.close()
