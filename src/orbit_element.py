from abc import ABC, abstractmethod


class OrbitElement(ABC):
    @abstractmethod
    def set_elements(self, elements):
        """
        Set the orbital elements of the satellite.
        """
        pass

    @abstractmethod
    def get_elements(self):
        """
        Return the orbital elements of the satellite.
        """
        pass


class CartesianElement(OrbitElement):
    def __init__(self, position_velocity=None):
        self._position_velocity = position_velocity

    def set_elements(self, position_velocity):
        if isinstance(position_velocity, tuple) and len(position_velocity) == 6:
            self._position_velocity = position_velocity
        else:
            raise ValueError("Position velocity must be a tuple of 6 elements.")

    def get_elements(self):
        return self._position_velocity


class KeplerianElement(OrbitElement):
    def __init__(self, kepler_elements=None):
        self._kepler_elements = kepler_elements

    def set_elements(self, kepler_elements):
        if isinstance(kepler_elements, tuple) and len(kepler_elements) == 6:
            self._kepler_elements = kepler_elements
        else:
            raise ValueError("Kepler elements must be a tuple of 6 elements.")

    def get_elements(self):
        return self._kepler_elements


# 使用例
cartesian = CartesianElement((7000, 0, 0, 0, 7.5, 0))
keplerian = KeplerianElement((10000, 0.01, 5, 100, 50, 0))

print("Cartesian Elements:", cartesian.get_elements())
print("Keplerian Elements:", keplerian.get_elements())
