#importing
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv

#Reading the file and converting it into a list
dataFrames = pd.read_csv("medium_data.csv")
data = dataFrames["claps"].tolist()

#Finding the mean of the complete data(population data)
populationMean = statistics.mean(data)
print("Population mean is :- ", populationMean)

#Finding the mean of 30 sample data points
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)    

    return mean

#Code to scale and plot the list of mean of the 100 different datasets
def showFigure(meanList):
    #Calculating the mean of the mean of the samples
    mean = statistics.mean(meanList)       
    print("Mean of sampling distribution is :- ", mean)

    figure = ff.create_distplot([meanList], ["Claps"], show_hist = False)
    figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "MEAN"))
    figure.show()

#Calculating the mean of the above 30 samples 100 times
def setup():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(30)        
        meanList.append(setOfMeans)
    #Calling the function
    showFigure(meanList)   

setup()      
