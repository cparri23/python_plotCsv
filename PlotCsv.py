import altair as alt
import numpy as np
import pandas as pd
import glob 
import csv
import os
from bs4 import BeautifulSoup

allCSV = glob.glob("*.csv")
htmlNames = glob.glob("*.html")

for name in htmlNames:
	os.remove(name)

x = []
y = []
xIndex = 0
yIndex = 2

xLabel = "x"
yLabel = "y"

for csvFile in allCSV:
	fileName = csvFile[:-4]
	with open(csvFile) as csvObj:
		reader = csv.reader(csvObj, delimiter=',')
		header = next(reader)
		
		try:
			print("No header for x.")
		except ValueError:
			xLabel = (float)(header[xIndex])
		
		try:
			yLabel = (float)(header[yIndex])
		except ValueError:
			print("No header for y.")		
		
		for row in reader:
			try:
				x.append(float(row[xIndex]))
				y.append(float(row[yIndex]))
			except ValueError:
				print("invalid point ignored - could be header.")
		
	source = pd.DataFrame({
	  xLabel: x,
	  yLabel: y
	})

	alt.Chart(source).mark_line().encode(
		x=xLabel,
		y=yLabel
	).save(fileName + ".html")
	
	x = []
	y = []
	
htmlNames = glob.glob("*.html")
htmlFile = open(htmlNames[0], 'a')
allGraphsHTML = BeautifulSoup(htmlFile)

