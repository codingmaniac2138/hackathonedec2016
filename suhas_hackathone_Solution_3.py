#SOLUTION of PROBLEM :3
import math
num_people = int(raw_input("Enter the number of people comming for wedding:"))

#run loop for takin locations of number of people entered
locations = []
def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

for i in xrange(num_people):

    #take people locations
    location_list = (raw_input("Enter the locations of people:").split(','))

    # get all inputs in location list
    locations.append(location_list)

    print(locations)
    for i in range(len(locations)):

        for i in locations:
            print i

                # dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
