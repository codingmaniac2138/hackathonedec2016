#SOLUTION of PROBLEM :3
import math
num_people = int(raw_input("Enter the number of people comming for wedding:"))

#run loop for takin locations of number of people entered
locations = []


for i in xrange(num_people):

    #take people locations
    location_list = (raw_input("Enter the locations of people:").split(','))
    location_list= ' '.join(location_list)
    # get all inputs in location list
    locations.append(location_list)
    oInput = ["9.5 7.5", "10.2 19.1", "9.7 10.2"]

    # parse inputs
    inp = [(float(j[0]), float(j[1])) for j in [i.split() for i in locations]]

    # initialize results with a really large value
    min_distance = float('infinity')
    min_pair = None

    # loop over inputs
    length = len(inp)
    for i in xrange(length):
        for j in xrange(i+1, length):
            point1 = inp[i]
            point2 = inp[j]

            # get distance between all the pairs
            distance = math.hypot(point1[0] - point2[0], point1[1] - point2[0])
            print distance, point1,point2

            # finding distance between points
            if math.hypot(point1[0] - point2[0], point1[1] - point2[0]) < min_distance:
                min_pair = [point1, point2]

                distance = math.hypot(point1[0] - point2[0], point1[1] - point2[0])
                # print min_pair,"ppppppppppppppppp"