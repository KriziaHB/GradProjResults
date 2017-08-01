# Student: Krizia Houston Buck
# Faculty: Dr. Emre Celebi
# University of Central Arkansas
# Summer 2017
# Graduate Project

# Analyze Results





# read info from files #
def fileInfo(results):
    # print( results[0].readlines() )
    x = 2

    # all output files per Results file for copying over into Excel
    fnSSE = "Metrics_SSE_" + str(x) + ".txt"
    outSSE = open(fnSSE, "w")
    fnMSE = "Metrics_MSE_" + str(x) + ".txt"
    outMSE = open(fnMSE, "w")
    fnMAE = "Metrics_MAE_" + str(x) + ".txt"
    outMAE = open(fnMAE, "w")
    fnTime = "Metrics_Time_" + str(x) + ".txt"
    outTime = open(fnTime, "w")

    for y in range(0,3):
        print(results[x].readline())


    # print to new file so I can take metric I need
    for line in results[x]:
        # list from line split by commas
        l = line.split(",")
        print(l)

        sse = l[5]
        mse = l[6]
        mae = l[7].split("-")
        t = mae[1].split("*")


        # add to output metric files
        outSSE.write(str(sse) + "\n")
        outMSE.write(str(mse) + "\n")
        outMAE.write(str(mae[0]) + "\n")
        outTime.write(str(t[0]) + "\n")
    # end of image results for loop


    # close files for analysis after
    outSSE.close()
    outMSE.close()
    outMAE.close()
    outTime.close()

# end of fileInfo #



# Call Everything from Main #
def main():
    print("Krizia Houston Buck - UCA Summer 2017 - Graduate Project - Dr. Emre Celebi")

    # new file called Results.txt for all user input and elapsed times
    output = open("Final_Results.txt", "w")
    output.write("Krizia Houston Buck - UCA Summer 2017 - Graduate Project - Dr. Emre Celebi \n\n")

    # open original results files
    results = []
    for x in range(1,9):
        fn = "Results_" + str(x) + ".txt"
        r = open(fn, "r")
        results.append(r)
    # end for accessing results files


    print(len(results))

    # separate out all metrics
    fileInfo(results)
# end of main #



# Call Main #
if __name__ == '__main__':
    main()
# end of program #