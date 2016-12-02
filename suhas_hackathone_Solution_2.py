#SOLUTION of PROBLEM :2
#take input testcases, run the loop for number of test cases asked
test_cases = int(raw_input("Enter the number of test cases:"))
for i in xrange(test_cases):

    #take start and destiantion input from the user
    start_destination = raw_input("Enter the Start and Destination:").split(',')
    start, destination = map(int, start_destination)

    #declare a count for counting the steps
    count = 0

    #check if destination is less then start
    if destination <= start:
        print "The number Of minimum steps are:", (start - destination)

    else:

        # keep on checking for destination is greater then start till the logic ends
        while destination >= start:
            if (destination % 2) != 0:
                destination += 1
            else:
                destination /= 2

            #increase the count till we get remainder as zero
            count += 1

            #if start and destination are same the ask user for new input
            if destination == start:
                print "You are on your destination, Kindly try with different input"
                break
        print "The number Of minimum steps are:", count + start - destination
