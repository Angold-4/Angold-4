from matplotlib import pyplot as plt
import EcoSysterm


def Test(eco, term, fish, bear):
    X = []
    YF = []
    YB = []
    F = 0
    B = 0
    TERMS = term
    EcoSysterm.set_eco(eco)
    for j in range(fish):
        EcoSysterm.Fish().goto()

    for j in range(bear):
        EcoSysterm.Bear().goto()

    for i in range(TERMS):
        """Cycle"""
        for j in EcoSysterm.ecosysterm:
            if isinstance(j, EcoSysterm.Bear):
                B += 1
                j.M_S()
            elif isinstance(j, EcoSysterm.Fish):
                F += 1
                j.M_S()
        X.append(i)
        YB.append(B)
        YF.append(F)
        F = 0
        B = 0

    """Draw"""

    plt.plot(X, YB)
    plt.plot(X, YF)
    plt.title("Species change(bear and fish)")
    plt.xlabel('Cycle times')
    plt.ylabel('Bears or Fishes')
    plt.legend(["Bear", "Fish"])
    plt.show()


if __name__ == "__main__":
    eco = int(input("Range of EcoSysterm: "))
    term = int(input("Cycle Terms: "))
    fish = int(input("Number of Fish: "))
    bear = int(input("Number of Bear: "))
    Test(eco, term, fish, bear)
