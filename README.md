This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Lane McCarty Project 2


Inside of the folder: 

- NearestNeighborClassification.py
- MeansClustering_driver.py
- KMeansClustering_functions.py
- ckd.csv


How to Run: 

For NearestNeighborClassification.py , just run the file. For a quick overview of what is in the file and what the file does: this file first determines which point in the training data is closest to the new point being tested by calculating the distance from the new point to the other dataset points and finding the point that is the minimum distance away (in this code is calculates the five closest points), then it returns the classification of the point as a 0 or a 1. It also produces two graphs, one without a random test point and one with a random test point that is shown in the color blue. 

For MeansClustering_driver.py , select the number of clusters desired by changing the " k = __" to a number (either a (1,2,3..). The file then will then print out a graph with the data in the desired clusters. It will also calculate the percentages of True Positives, False Positives, True Negatives, and False Negatives. 

For KMeansClustering_functions.py , this file does not need to be run as the functions inside of it are run by the previously described driver file. 

For ckd.csv , this file also does not need to be run as the data inside of it is used by the the other files. 


Functions inside NearestNeighborClassification.py: 

-def openckdfile():
takes no arguments, opens the ckd file then reads the data and returns three numpy arrays with the data.

-def normalizeData(glucose, hemoglobin, classification):
Takes the arguments glucose, hemoglobin, and classification. Normalizes each of the data sets into a unitless scale from 0 to 1. Returns the scaled values glucose, hemoglobin, and classification in an array.

-def graphData(glucose, hemoglobin, classification):
Graphs the scaled values of hemoglobin and glucose. It colors each point based on its classification. Takes three arguments glucose, hemoglobin, and classification.

-def createTestCase():
takes no arguments. Creates a random test case that falls within the min and max values of the training hemo and gluco data. Returns the values newhemo, newglu.

-def calculateDistanceArray(newglu, newhemo, glucose, hemoglobin):
Takes the arguments newglu, newhemo, glucose, and hemoglobin. returns the distance array which contains the distance calculated to the new point from each point in the existing dataset. 

-def nearestNeighborClassifier(newglu, newhemo, glucose, hemoglobin, classification):
Calls the distance function to find the min distance to the closest points to then read their classifications. returns the classification for the point (either a 0 or 1) based on the closest point. Returns an integer which is the class of the data point (test case).

-def graphTestCase(newhemo, newglu, glucose, hemoglobin, classification):
graphs the test case as well as the graphData. Takes 5 arguments total, the two integers from newhemo and newglu and three arrays glucose, hemoglobin and classification.

-def kNearestNeighborClassifier(k, newglu, newhemo, glucose, hemoglobin, classificiation):
this function takes 6 arguments, k is the number of neighbors, newglu, newhemo, glucose, hemoglobin, classificiatio. #It finds the classification of the test case based on the number of points around it (k). It also prints out the #array of the closest points as well as its overall classification.


Functions inside KMeansClustering_functions.py: 

-def openckdfile():
Takes no arguments, opens the ckd file then reads the data and returns three numpy arrays with the data.

-def normalizeData(glucose, hemoglobin, classification):
Takes the arguments glucose, hemoglobin, and classification. Normalizes each of the data sets into a unitless scale from 0 to 1. Returns the scaled values in an array.

-def select_centroids(k):
#this function creates k number of centroids for the set of data. It takes one
#argument k which is the number of centroids and returns a k by k array with the
#centroid points.

-def assign(array_centroids, glucose, hemoglobin):
assigns each data point a label based on which centroid it is closest to. takes three arguments array_centroids, glucose, and hemoglobin. It then returns a numpy array of arguments.

-def update(k, assignment, glucose, hemoglobin):
updates the location of each centroid based on the means of the data points assigned to that cluster. It takes four arguments k which is the number of clusters desired to use, assingment which is the array of assignments and glucose and hemoglobin. It then returns an array of updated centroids.

-def iterate(k, iterations):
this function repeats the Assign and Update steps until the end condition is met, basically running over and over again until an end is met. It takes 2 arguments, k which is the number of clusters desired and iterations which is the number of times the algorithm will run. It then returns the assignment array, final centroids, glucose, hemoglobin, and the classification.

-def graphingKMeans(glucose, hemoglobin, assignment, centroids):
graphs the training data, in the appropriate clusters, from the ckd file. It takes four arguments which are all arrays glucose, hemoglobin, assignment, and centroids. 

-def calculate(classification, assignment):
takes two arguments classification and and assignment. Determines how accurate the assignments are to the centroids by comparing the original classifcations to the assignments. If the classifications are the same then it returns a true positive or false positive, and if they are not the same then it returns a false positive or false negative. The function is counting the number of true pos/neg and false pos/neg then calculates the percentages and prints them out.



