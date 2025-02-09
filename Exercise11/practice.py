# {dictionary}
# keys:values
landmarks = {'Burj Khalifa': 830, 'Eiffel Tower': 330, 'London Eye': 135}

for index, landmark_name in enumerate(landmarks.keys(), start=1):
    print(f"{index:2d} {landmark_name:<12s} {landmarks[landmark_name]:} meters")
# index - pulls index from enumerate
# 2 - width/d - integer
# < left-align
# 12 - minimum width
# s - string format
# landmarks[landmarks_name] - retrieves the height of landmark
# meters - string added at the end
















