#Lane McCarty's step 4
#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random

#$$$$$$$$$$$$$$$$$$$$$$

def openckdfile():
#takes no arguments, opens the ckd file then reads the data and returns
#three numpy arrays with the data.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#$$$$$$$$$$$$$$$$$$$$$$
    
def normalizeData(glucose, hemoglobin, classification):
#Takes the arguments glucose, hemoglobin, and classification. 
#Normalizes each of the data sets into a unitless scale from 0 to 1. Returns
#the scaled values in an array.
    hemoglobin_scaled = (hemoglobin-3.1)/(17.8-3.1)
    glucose_scaled = (glucose-70)/(490-70)
    return glucose_scaled, hemoglobin_scaled, classification

#$$$$$$$$$$$$$$$$$$$$$$
    
def select_centroids(k):
#this function creates k number of centroids for the set of data. It takes one
#argument k which is the number of centroids and returns a k by k array with the
#centroid points.
    array_centroids = np.random.rand(k,2)
    return array_centroids

#$$$$$$$$$$$$$$$$$$$$$$$$
    
def assign(array_centroids, glucose, hemoglobin):
#assigns each data point a label based on which centroid it is closest to. 
#takes three arguments array_centroids, glucose, and hemoglobin. It then returns
#a numpy array of arguments
    l = array_centroids.shape[0]
    distance = np.zeros((l,(len(glucose))))
    assignment = np.zeros((len(glucose)))
    for x in range(l):
        gluc = array_centroids[x,1]
        hemo = array_centroids[x,0]
        distance[x] = np.sqrt(((hemo - hemoglobin)**2)+(gluc-glucose)**2)     
    assignment = np.argmin(distance, axis = 0)
    return assignment, distance

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def update(k, assignment, glucose, hemoglobin):
#updates the location of each centroid based on the means of the data points assigned to
#that cluster. It takes four arguments k which is the number of clusters desired to use, assingment 
#which is the array of assignments and glucose and hemoglobin. It then returns an array of updated centroids.
    centroids = np.zeros((k,2))
    centroid_hemoglobin = np.zeros((1))
    centroid_glucose = np.zeros((1))
    for x in range(centroids.shape[0]):
        centroid_hemoglobin = np.mean(hemoglobin[assignment == x])
        centroid_glucose = np.mean(glucose[assignment == x])
        centroids[x] = np.append(centroid_hemoglobin, centroid_glucose) 
    return centroids

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
def iterate(k, iterations):
#this function repeats the Assign and Update steps until the end condition is met, basically running
#over and over again until an end is met. It takes 2 arguments, k which is the number of 
#clusters desired and iterations which is the number of times the algorithm will run. 
#it then returns the assignment array, final centroids, glucose, hemoglobin, and the classification.
    glucose, hemoglobin, classification = openckdfile()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    centroids = select_centroids(k)
    while iterations != 0:
        assignment, distances = assign(centroids, glucose, hemoglobin)
        centroids = update(k, assignment, glucose, hemoglobin)
        iterations = iterations - 1
    return assignment, centroids, glucose, hemoglobin, classification

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def graphingKMeans(glucose, hemoglobin, assignment, centroids):
#graphs the training data, in the appropriate clusters, from the ckd file. It takes four arguments
#which are all arrays glucose, hemoglobin, assignment, and centroids. 
    plt.figure()
    for x in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment == x],glucose[assignment == x], ".", label = "Class " + str(x), color = rcolor)
        plt.plot(centroids[x, 0], centroids[x, 1], "X", markersize = 12, label = "Centroid " + str(x), color = rcolor)
    plt.title('CKD Training Set')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
    
def calculate(classification, assignment):
#takes two arguments classification and and assignment. Determines how accurate the assignments
#are to the centroids by comparing the original classifcations to the assignments. If the classifications
#are the same then it returns a true positive or false positive, and if they are not the same then it returns
#a false positive or false negative. The function is counting the number of true pos/neg and false pos/neg
#then calculates the percentages and prints them out. 
    truepos = 0
    falsepos = 0
    trueneg = 0
    falseneg = 0
    CKD = 0
    noCKD = 0 
    for x in range(158):
        if classification[x] == assignment[x] == 0:
            truepos = truepos + 1
            CKD = CKD + 1
        elif classification[x] == 1 and assignment[x] == 0:
            falsepos = falsepos + 1
            noCKD = noCKD + 1
        elif classification[x] == assignment[x] == 1:
            trueneg = trueneg + 1
            noCKD = noCKD + 1
        elif classification[x] == 0 and assignment[x] == 1:
            falseneg = falseneg + 1
            CKD = CKD + 1

    print("Rate of True Positives: " + str((truepos/CKD)*100) + ' %')         
    print("Rate of False Positives: " + str((falsepos/noCKD)*100) + ' %')
    print("Rate of True Negatives: " + str((trueneg/noCKD)*100) + ' %') 
    print("Rate of False Negatives: " + str((falseneg/CKD)*100) + ' %') 
