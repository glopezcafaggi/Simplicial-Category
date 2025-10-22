from core.utils import Utils
from models.simplex import Simplex
import numpy as np

class Morphism:
    """Morphism class: represents a morphism in the simplex category
    
    Attributes
    -------
    domain : Simplex
        The domain object in the simplex category representing the order set  [M]= {0<1<2<...<N}
    codomain : Simplex
        The codomain object in the simplex category representing the order set  [M]= {0<1<2<...<M}
    mapping: np.array
        The order preserving set-category mapping rule among the order sets [N] to [M]
    matrix: np.array
        The 2 matrix that represents the morphism under the canonical embedding to Real Vector spaces with the canonical basis.

    Methods
    """
    
    def __init__(self, N: Simplex, M:Simplex, mapping: np.array):
        self.__domain = N
        self.__codomain = M
        self.__mapping = mapping
        self.__matrix = Utils.matrix_morphism(N.size, M.size ,mapping)

    @property
    def domain(self):
        return self.__domain
    
    @property
    def codomain(self):
        return self.__codomain
    
    @property
    def matrix(self):
        return self.__matrix
    @property
    def mapping(self):
        return self.__mapping


    def __str__(self):
        pass

class Indentity(Morphism):
    def __init__(self, N: Simplex):
        super().__init__(N,N,N.array)