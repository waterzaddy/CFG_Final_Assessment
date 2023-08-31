## CODING CHALLENGE
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""


class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance_to_earth = abs(self.distance_from_sun - 147_000_000)
        return {"distance to earth": distance_to_earth}


"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""


class Mercury(Planet):
    def __init__(self, distance_from_sun, planet_type):
        name = "Mercury"
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        return "Happy New Year, Mercury! A year lasts 88 Earth days."


if __name__ == "__main__":
    mercury = Mercury(58_000_000, 'Terrestrial')

    # Attributes of Mercury
    print(f"Name: {mercury.name}")
    print(f"Distance from Sun: {mercury.distance_from_sun} km")
    print(f"Planet Type: {mercury.planet_type}")
    print(mercury.get_distance_to_earth())
    print(Mercury.happy_new_year())


"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""


class Jupiter(Planet):
    def __init__(self, distance_from_sun, planet_type, number_of_moons):
        name = "Jupiter"
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        return "Happy New Year, Jupiter! A year lasts 4383 Earth days."


if __name__ == "__main__":
    # Creating an instance of the Jupiter class
    jupiter = Jupiter(779_000_000, 'Gas Giant', 80)

    # Printing attributes and methods for Jupiter
    print(f"Name: {jupiter.name}")
    print(f"Distance from Sun: {jupiter.distance_from_sun} km")
    print(f"Planet Type: {jupiter.planet_type}")
    print(f"Number of Moons: {jupiter.number_of_moons}")
    print(jupiter.get_distance_to_earth())
    print(Jupiter.happy_new_year())






