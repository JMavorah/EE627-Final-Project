import csv

#train_data = open('trainItem2.txt')
#track_data = open('trackData2.txt')

#format test data into dictionary, where key is userID and values are the six
#songs to be recommended/not recommended:
with open('testItem2.txt') as test_data:
    users_tracks = {}
    tracks = [None]*6
    userID = ' '
    index = 0
    for line in test_data:
        if '|' in line:
            index = 0
            x = line.split('|')
            userID = x[0].rstrip()
        else:
            tracks[index] = line.rstrip()
            index += 1
            users_tracks[userID] = tracks

print(users_tracks)

with open('trainItem2.txt') as train_data:
    train_contents = train_data.read()

with open('trackData2.txt') as track_data:
    track_contents = track_data.read()



#with open('hw5.csv', newline='') as csvfile:
#    csvwriter = csv.writer(csvfile)
#    csvwriter.writerows()


#train_data.close()
#track_data.close()
