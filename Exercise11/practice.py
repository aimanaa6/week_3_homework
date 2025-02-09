landmarks = {'Burj Khalifa': 830, 'Eiffel Tower': 330, 'London Eye': 135}

for index, landmark_name in enumerate(landmarks.keys(), start=1):
    print(f"{index:2d} {landmark_name:<12s} {landmarks[landmark_name]:} meters")



# for landmarks_name in landmarks.keys():
#     print(landmarks_name)

# for landmarks_length in landmarks.keys():
#     print(landmarks_length)
#
#
# for index, landmarks in enumerate(landmarks.keys(), start=1):
#     print(f"{index:2d} {landmarks:<12s} {landmarks[landmarks_name]:,} people")
# # #
# #
# for index, landmarks in enumerate(landmarks.keys(), start=1):
#     # print(index, landmarks_name, planets[landmarks_name])
#     print(f"{index:2d} {landmarks_name:<10s} {landmarks:06.2f}")
#
#     for index, planet_name in enumerate(planets.keys(), start=1):
#         # print(index, planet_name, planets[planet_name])
#         print(f"{index:2d} {planet_name:<10s} {planets[planet_name]:06.2f} Gm")
