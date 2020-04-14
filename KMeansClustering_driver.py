#Please place your FUNCTION code for step 4 here.


import KMeansClustering_functions as kmc #Use kmc to call your functions

#Number of clusters 
k=2

glucose, hemoglobin, classification = kmc.openckdfile()
glucose, hemoglobin, classification = kmc.normalizeData(glucose, hemoglobin, classification)
assignment, centroids, glucose, hemoglobin, classification = kmc.iterate(k,70)
kmc.graphingKMeans(glucose, hemoglobin, assignment, centroids)
kmc.calculate(classification, assignment)

