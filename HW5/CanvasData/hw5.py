import csv


with open('.txt') as test_data:
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






#with open('hw5.csv', newline='') as csvfile:
#    csvwriter = csv.writer(csvfile)
#    csvwriter.writerows()
