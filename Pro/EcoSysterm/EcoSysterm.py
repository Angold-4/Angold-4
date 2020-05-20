from random import randint
from matplotlib import pyplot as plt


def set_eco(r):
    global RANGE
    global ecosysterm
    RANGE = r
    ecosysterm = [None]*r


class Animal:
    """Base class"""

    def __init__(self):
        G = randint(0, 1)
        S = randint(0, 9)
        D = randint(0, RANGE-1)
        _genderdict = {0: False, 1: True}
        self._gender = _genderdict[G]
        self._strength = S
        self._addr = D

    def _set_gender(self, TF):
        if TF is True or TF is False:
            self._gender = TF
        else:
            print("Unsupported Gender(True or False)")

    def get_gender(self):
        return self._gender

    def get_strength(self):
        return int(self._strength)

    def M_S(self):
        """Move or Stay"""
        MoS = randint(0, 1)
        if MoS == 0:
            """Stay"""
            pass
        else:
            ecosysterm[self._addr] = None
            if self._addr == RANGE-1:
                self._addr -= 1
            elif self._addr == 0:
                self._addr += 1
            else:
                A = randint(0, 1)
                if A == 0:
                    """Previous"""
                    self._addr -= 1
                else:
                    """Next"""
                    self._addr += 1
            """Move"""
            self.goto()


class Bear(Animal):

    def goto(self):
        """Move to Other Addr in Eco"""
        if ecosysterm[self._addr] is None or isinstance(ecosysterm[self._addr], Fish):
            ecosysterm[self._addr] = self
        else:
            if ecosysterm[self._addr].get_gender() == self.get_gender():
                if ecosysterm[self._addr].get_strength() < self.get_strength():
                    ecosysterm[self._addr] = self
            else:
                """Opposite Sex Created a New Child"""
                Bear().goto()


class Fish(Animal):

    def goto(self):
        """Move to Other Addr in Eco"""
        if ecosysterm[self._addr] is None:
            ecosysterm[self._addr] = self
        elif isinstance(ecosysterm[self._addr], Bear):
            """Be Eaten"""
            pass
        else:
            if ecosysterm[self._addr].get_gender() == self.get_gender():
                if ecosysterm[self._addr].get_strength() < self.get_strength():
                    ecosysterm[self._addr] = self

            else:
                """Opposite Sex Created a New Child"""
                Fish().goto()
