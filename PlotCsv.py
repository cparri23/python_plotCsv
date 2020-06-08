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
charts = []

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
			xLabel = (float)(header[xIndex])
		except ValueError:
			print("No header for x.")
		
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

	tempChart = alt.Chart(source).mark_line().encode(
		x=xLabel,
		y=yLabel
	).properties(title=fileName + ".html")
	charts.append(tempChart)
	tempChart.save(fileName + ".html")
	
	x = []
	y = []
	
allCharts = charts[0]	
for i in range(1, len(charts)):
	allCharts = allCharts & charts[i]
	
allCharts.save("allCharts.html")

