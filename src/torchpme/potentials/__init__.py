from .combined import CombinedPotential
from .coulomb import CoulombPotential
from .inversepowerlaw import InversePowerLawPotential
from .potential import Potential
from .potential_dipole import EfieldlDipole
from .spline import SplinePotential

__all__ = [
    "CombinedPotential",
    "CoulombPotential",
    "InversePowerLawPotential",
    "Potential",
    "SplinePotential",
    "EfieldlDipole",
]
