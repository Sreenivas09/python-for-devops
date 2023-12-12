import sys

var = sys.argv[1]

if var == "AWS":
    print("Choose a EC2 instance to create the PAAS services")
elif var == "Azure":
    print("Choose a Resource group to create the PAAS services")  
elif var == "GCP":
    print("Choose a gcp Resource group to create the PAAS services")      
else:
    print("Please choose a correct cloud environment to utilize PAAS services")    