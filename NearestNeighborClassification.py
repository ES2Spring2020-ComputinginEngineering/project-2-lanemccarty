# Lane McCarty's step 2 and 3 


import numpy as np
import matplotlib.pyplot as plt
import random



# FUNCTIONS
def openckdfile():
#takes no arguments, opens the ckd file then reads the data and returns
#three numpy arrays with the data.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

#$$$$$$$$$$$$$$$$$$$$$$$$

def normalizeData(glucose, hemoglobin, classification):
#Takes the arguments glucose, hemoglobin, and classification. 
#Normalizes each of the data sets into a unitless scale from 0 to 1. Returns
#the scaled values in an array.
    hemoglobin_scaled = (hemoglobin-3.1)/(17.8-3.1)
    glucose_scaled = (glucose-70)/(490-70)
    return glucose_scaled, hemoglobin_scaled, classification

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def graphData(glucose, hemoglobin, classification):
#Graphs the scaled values of hemoglobin and glucose. It colors each point based on
#its classification.
    plt.figure()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin,classification)
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.title("Hemoglobin vs Glucose")
    plt.show()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def createTestCase():
#takes no arguments. Creates a random test case that falls within the min 
#and max values of the training hemo and gluco data.
    newglu = random.random()
    newhemo = random.random()
    return newhemo, newglu

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def calculateDistanceArray(newglu, newhemo, glucose, hemoglobin):
#returns the distance array which contains the distsance calculated to the new point from each
#point in the existing dataset. 
    distance = np.sqrt(((newglu-glucose)**2)+(newhemo-hemoglobin)**2)
    return distance

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def nearestNeighborClassifier(newglu, newhemo, glucose, hemoglobin, classification):
#returns the classification for the point (either a 0 or 1) based on the closest point. Returns 
#an integer which is the class of the data point (test case).
    min_index = np.argmin(distance)
    nearest_class = classification[min_index]
    return nearest_class

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
def graphTestCase(newhemo, newglu, glucose, hemoglobin, classification):
#graphs the test case as well as the graphData. Takes 5 arguments total, the two integers 
#from newhemo and newglu and three arrays glucose, hemoglobin and classification.
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot([newhemo], [newglu], marker = 'o', markersize = 5, color = 'blue')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin vs Glucose")
    plt.legend()
    plt.show()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def kNearestNeighborClassifier(k, newglu, newhemo, glucose, hemoglobin, classificiation):
#this function takes 6 arguments, k is the number of neighbors. It finds the classification
#of the test case based on the number of points around it (k). It also prints out the array 
#of the closest points as well as its overall classification.
    distance_array = calculateDistanceArray(newglu, newhemo, glucose, hemoglobin)
    sortedind = np.argsort(distance_array)
    k_indices = sortedind[:k]
    k_classifications = classification[k_indices]
    k_class = np.median(k_classifications)
    print("closest points:", k_classifications)
    print("classifcation:", k_class)
    return k_class

k = 5


# MAIN SCRIPT

glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
graphData(glucose, hemoglobin, classification)
newglu, newhemo = createTestCase()
distance = calculateDistanceArray(newglu, newhemo, glucose, hemoglobin)
nearest_class = nearestNeighborClassifier(newglu, newhemo, glucose, hemoglobin, classification)
graphTestCase(newhemo, newglu, glucose, hemoglobin, classification)
kNearestNeighborClassifier(k, newglu, newhemo, glucose, hemoglobin, classification)






