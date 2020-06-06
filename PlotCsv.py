import altair as alt
import numpy as np
import pandas as pd
import glob 
import csv

allCSV = glob.glob("*.csv")

x = []
y = []
xIndex = 0
yIndex = 2

xLabel = "x"
yLabel = "y"

for csvFile in allCSV:
	fileName = csvFile[:-4]
	print(csvFile)
	with open(csvFile) as csvObj:
		reader = csv.reader(csvObj, delimiter=',')
		header = next(reader)
		
		try:
			print("No header for x.")
		except ValueError:
			xLabel = header[xIndex]
		
		try:
			print("No header for y.")
		except ValueError:
			yLabel = header[yIndex]		
		
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
