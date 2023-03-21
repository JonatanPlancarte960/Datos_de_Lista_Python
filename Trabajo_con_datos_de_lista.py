planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planet_input = input('Enter the Name of the Planet, Starting with Capital Letter: ')
planet_index = planets.index(planet_input)

print("Here are the planets closer to the Sun than " + planet_input)
print(planets[0:planet_index])

print("Here are the planets further to the Sun than " + planet_input)
print(planets[planet_index + 1:])