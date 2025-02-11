# {dictionary}
# keys:values - landmark names:heights
landmarks = {'Burj Khalifa': 830, 'Eiffel Tower': 330, 'London Eye': 135}

for index, landmark_name in enumerate(landmarks.keys(), start=1):
    print(f"{index:2d} {landmark_name:<12s} {landmarks[landmark_name]:} meters")
# loops through the dictionary keys one by one
# index gives a number starting from 1
# {index:2d} = index is a two digit number
# {<12s} - < left aligned, with minimum 12 character width
# s - string format
# landmarks[landmarks_name] - retrieves the height of landmark
# meters - string (unit) added at the end
















