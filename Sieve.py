import numpy as np

f = open("planet_list.csv","r")

planets = []

for line in f:
    planet = line.split(',')
    new_planet = [planet[i] for i in [1, 5, 9, 13] if planet[i] != '']
    if len(new_planet) == 4:
        planets.append(new_planet)

a = [float(planet[0]) for planet in planets]
M = [float(planet[1]) for planet in planets]
T = [float(planet[2]) for planet in planets]
R = [float(planet[3]) for planet in planets]

L = [(R[i])**2 * (T[i]/5778)**4 for i in range(0,len(planets))]

albedo = 0
lower_mass = 0.5
upper_mass = 20
    
giants = []
habitable_giants = []    

for i in range(0,len(planets)):
    if M[i] > lower_mass and M[i] < upper_mass:
        giants.append(M[i])
        r_inner = np.sqrt(0.92*L[i]*(1 - albedo))
        r_outer = np.sqrt(3.21*L[i]*(1 - albedo))
        if r_inner < a[i] and a[i] < r_outer:
            habitable_giants.append(planets[i])

print("There are %s exoplanets with enough parameters." %len(planets))
print("There are %s giant planets." %len(giants))
print("The fraction of giant planets in the habitable zone is %.2f%%." %(len(habitable_giants)/len(giants)*100))