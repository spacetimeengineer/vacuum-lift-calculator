#!/usr/bin/env python3

# Writer: Michael.C Ryan 
# Email: spacetime.engineer@gmail.com

import math
from sympy import *

# Class for creating vacuum chamber objects for use in effective antigravity; a balloon.
class SphereVacuumPod:

    # Run at object creation.
    def __init__(self, material_density, thickness, interior_radius, price_per_gram):

        # Initialization.        
        self.material_density = material_density       # In units of grams per centimeter cubed.
        self.thickness = thickness                     # In units of centimeters.
        self.interior_radius = interior_radius         # In units of centimeters.
        self.relative_vacuum_density = -0.00128        # In units of grams per centimeter cubed.
        self.price_per_gram = price_per_gram           # In units of USD.

        # Prints essential information.
        print("Totals")
        print("====================")
        print("Total Effective Mass        : " + str(self.get_effective_mass()*0.001) + " kg")
        print("Total Material Cost         : $" + str(self.get_material_price()))
        print("")

    def get_effective_mass(self):
        # Not a true negative mass but it behaves exactly as if it were. Interesting from the viewpoint that mass need only be effective to be true.
        effective_negative_mass = self.relative_vacuum_density * 4 / 3 * math.pi * self.interior_radius ** 3
        # print("Effective Vacuum Mass : " + str(0.001 * negative_mass) + " kg")
        effective_mass = effective_negative_mass + self.get_vacuum_chamber_mass()		
        # print("Max lift mass: " + str(max_lift_mass) + " grams")
        return effective_mass					

    def get_vacuum_chamber_mass(self):
        # Takes the volume of a sphere with a particular density minus the mass of another sphere with the same material density but with a radius equal to the former minus the thickness.
        vacuum_chamber_mass = self.material_density * 4 / 3 * math.pi * ( ( self.interior_radius + self.thickness ) ** 3 - self.interior_radius ** 3)
        # print("Total Vacuum Chamber Mass   : " + str(0.001 * vacuum_chamber_mass) + " kg")
        return vacuum_chamber_mass	

    def get_material_price(self):
        # Returns total material cost.
        return self.price_per_gram * self.get_vacuum_chamber_mass()

# Class for creating vacuum chamber objects for use in effective antigravity; a balloon.
class TetrahedronVacuumChamber:

    # Run at object creation.
    def __init__(self, material_density, thickness, interior_triangle_side_length, price_per_gram):

        # Initialization.        
        self.material_density = material_density                                   # In units of grams per centimeter cubed.
        self.thickness = thickness                                                 # In units of centimeters.
        self.interior_triangle_side_length = interior_triangle_side_length         # In units of centimeters.
        self.relative_vacuum_density = -0.00128                                    # In units of grams per centimeter cubed.
        self.price_per_gram = price_per_gram                                       # In units of USD.

        # Prints essential information.
        print("Totals")
        print("====================")
        print("Total Effective Mass        : " + str(self.get_effective_mass()*0.001) + " kg")
        print("Total Material Cost         : $" + str(self.get_material_price()))
        print("")

    def get_effective_mass(self):

        # Not a true negative mass but it behaves exactly as if it were. Interesting from the viewpoint that mass need only be effective to be true.
        effective_negative_mass = self.relative_vacuum_density * self.get_tetrahedron_volume(self.interior_triangle_side_length)
        # print("Effective Vacuum Mass : " + str(0.001 * negative_mass) + " kg")
        effective_mass = effective_negative_mass + self.get_vacuum_chamber_mass()		
        # print("Max lift mass: " + str(max_lift_mass) + " grams")
        return effective_mass					

    def get_tetrahedron_volume(self, side_length):
        # Returns tetrahedron volume.
        return side_length ** 3 / ( 6 * 2 ** ( 0.5 ))

    def get_vacuum_chamber_mass(self):
        # Takes the volume of a sphere with a particular density minus the mass of another sphere with the same material density but with a radius equal to the former minus the thickness.
        vacuum_chamber_mass = self.material_density * ( self.get_tetrahedron_volume( self.interior_triangle_side_length + self.thickness ) - self.get_tetrahedron_volume(self.interior_triangle_side_length ))
        print("Total Vacuum Chamber Mass   : " + str(0.001 * vacuum_chamber_mass) + " kg")
        return vacuum_chamber_mass	

    def get_material_price(self):
        # Returns total material cost.
        return self.price_per_gram * self.get_vacuum_chamber_mass()

# Main loop.
while (True):

    # Useful data table.
    print("")
    print("Reference")
    print("=========")
    print("Density of aluminium = 2.7 g / cm ^ 3.")
    print("Density input is in g / cm ^ 3")
    print("Radius and thickness input are in cm.")
    print("Cost per gram input is in USD / cm ^ 3.")
    print("Cost of aluminium is 0.00691 / cm ^ 3.")
    print("")

    print("Input")
    print("=====")
    print("What shape is the vacuum chamber? sphere = s, tetrahedron = t")
    shape = input("> ")

    if (shape == "s"):

        # Units in grams, centimeters and seconds.
        print("What is the density ( in grams ) of the material used to construct the vacuum chamber?")
        material_density = input("> ")
        print("What is the thickness ( in cm ) of the spherical chamber wall?")
        thickness = input("> ")
        print("What is the interior radius ( in cm ) of the vacuum chamber?")
        interior_radius = input("> ")
        print("What is the price per gram ( in USD ) of material?")
        price_per_gram = input("> ")
        print("")

        # Creates vacuum chamber object.
        SphereVacuumPod(float(material_density), float(thickness),  float(interior_radius), float(price_per_gram))

    elif(shape == "t"):

        # Units in grams, centimeters and seconds.
        print("What is the density ( in grams ) of the material used to construct the vacuum chamber?")
        material_density = input("> ")
        print("What is the thickness ( in cm ) of the tetrahedron chamber wall?")
        thickness = input("> ")
        print("What is the interior side length ( in cm ) of the tetrahedron vacuum chamber?")
        interior_triangle_side_length = input("> ")
        print("What is the price per gram ( in USD ) of material?")
        price_per_gram = input("> ")
        print("")

        # Creates vacuum chamber object.
        TetrahedronVacuumChamber(float(material_density), float(thickness),  float(interior_triangle_side_length), float(price_per_gram))
    else:
        pass

    print("END")
    print("===")
