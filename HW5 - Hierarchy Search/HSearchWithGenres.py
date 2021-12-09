import numpy as np
import csv

test_file = 'testTrack_hierarchy.txt'
train_file = 'trainIdx2_matrix.txt'
output_file = 'outputH2.txt'
output_csv = 'outputH2.csv'

fTest = open(test_file, 'r') #open input files with read permission
fTrain = open(train_file, 'r')
Trainline = fTrain.readline()
fOut = open(output_file, 'w') #open output files with write
fOutCSV = open(output_csv, 'w')

trackID_vec=[0]*6
albumID_vec=[0]*6
artistID_vec=[0]*6

#-----------------------------------------------------------------------------------
genre1_vec=[0]*6
genre2_vec=[0]*6
genre3_vec=[0]*6
genre4_vec=[0]*6
genre5_vec=[0]*6
genre6_vec=[0]*6
genre7_vec=[0]*6
#-----------------------------------------------------------------------------------

lastUserID=-1

user_rating_inTrain=np.zeros(shape=(6,10))

for line in fTest:
    arr_test = line.strip().split('|')
    userID = arr_test[0]
    trackID = arr_test[1]
    albumID = arr_test[2]
    artistID = arr_test[3]

    #------------------------------------------------------------------------------
    if(len(arr_test) > 4): genre1 = arr_test[4]
    if(len(arr_test) > 5): genre2 = arr_test[5]
    if(len(arr_test) > 6): genre3 = arr_test[6]
    if(len(arr_test) > 7): genre4 = arr_test[7]
    if(len(arr_test) > 8): genre5 = arr_test[8]
    if(len(arr_test) > 9): genre6 = arr_test[9]
    if(len(arr_test) > 10): genre7 = arr_test[10]
    #------------------------------------------------------------------------------

    if userID!= lastUserID:
        ii=0
        user_rating_inTrain=np.zeros(shape=(6,10))

    trackID_vec[ii]=trackID
    albumID_vec[ii]=albumID
    artistID_vec[ii]=artistID

    #-----------------------------------------------------------------------------
    if(len(arr_test) > 4): genre1_vec[ii]=genre1
    if(len(arr_test) > 5): genre2_vec[ii]=genre2
    if(len(arr_test) > 6): genre3_vec[ii]=genre3
    if(len(arr_test) > 7): genre4_vec[ii]=genre4
    if(len(arr_test) > 8): genre5_vec[ii]=genre5
    if(len(arr_test) > 9): genre6_vec[ii]=genre6
    if(len(arr_test) > 10): genre7_vec[ii]=genre7
    #-----------------------------------------------------------------------------

    ii=ii+1
    lastUserID=userID

    if ii==6:
        while (Trainline):
            arr_train = Trainline.strip().split('|')
            trainUserID=arr_train[0]
            trainItemID=arr_train[1]
            trainRating=arr_train[2]
            Trainline=fTrain.readline()

            if trainUserID < userID:
                continue
            if trainUserID == userID:
                for nn in range(0,6):
                    if trainItemID==albumID_vec[nn]:
                        user_rating_inTrain[nn,0]=trainRating
                    if trainItemID==artistID_vec[nn]:
                        user_rating_inTrain[nn,1]=trainRating

                    #-------------------------------------------------------------
                    if trainItemID==genre1_vec[nn]:
                        user_rating_inTrain[nn,3]=trainRating
                    if trainItemID==genre2_vec[nn]:
                        user_rating_inTrain[nn,4]=trainRating
                    if trainItemID==genre3_vec[nn]:
                        user_rating_inTrain[nn,5]=trainRating
                    if trainItemID==genre4_vec[nn]:
                        user_rating_inTrain[nn,6]=trainRating
                    if trainItemID==genre5_vec[nn]:
                        user_rating_inTrain[nn,7]=trainRating
                    if trainItemID==genre6_vec[nn]:
                        user_rating_inTrain[nn,8]=trainRating
                    if trainItemID==genre7_vec[nn]:
                        user_rating_inTrain[nn,9]=trainRating
                    #-------------------------------------------------------------

            if trainUserID > userID:
                for nn in range(0,6):
                    outStr=str(userID) + '|' + str(trackID_vec[nn]) + '|' + str(user_rating_inTrain[nn,0]) + '|' + str(user_rating_inTrain[nn,1]) \
                        + str(user_rating_inTrain[nn,2]) + '|' + str(user_rating_inTrain[nn,3])+ '|' + str(user_rating_inTrain[nn,4]) \
                            + '|' + str(user_rating_inTrain[nn,5])+ '|' + str(user_rating_inTrain[nn,6])+ '|' + str(user_rating_inTrain[nn,7]) \
                                + '|' + str(user_rating_inTrain[nn,8])+ '|' + str(user_rating_inTrain[nn,9])
                    fOut.write(outStr + '\n')
                    outStr=str(userID) + ',' + str(trackID_vec[nn]) + ',' + str(user_rating_inTrain[nn,0]) + ',' + str(user_rating_inTrain[nn,1]) \
                        + str(user_rating_inTrain[nn,2]) + ',' + str(user_rating_inTrain[nn,3])+ ',' + str(user_rating_inTrain[nn,4]) \
                            + ',' + str(user_rating_inTrain[nn,5])+ ',' + str(user_rating_inTrain[nn,6])+ ',' + str(user_rating_inTrain[nn,7]) \
                                + ',' + str(user_rating_inTrain[nn,8])+ ',' + str(user_rating_inTrain[nn,9])
                    fOutCSV.write(outStr + '\n')
                break


fTest.close()
fTrain.close()
