import numpy as np

class Simplex:
    """ Simplex class: represents an object in the simplex categoy, i.e. [n]= {0<1<2<..<n} for an natural n
    
    Attributes
    -----
    array: np.array
        order array of size representing [n] i.e. [0,1,2,..., n]
    size: int
        the cardinality of the order set [n], i.e n+1
    label: int
        the name of [n]  the largest element in the order set [n], i.e. n
    zero: int
        the least element of the order set [n], i.e. 0
    """
    
    def __init__(self, n: int):
        self.__array = np.arange(n+1)
        self.__size = len(self.__array)
        self.__label = n
        self.__zero = self.__array[0]
    
    @property
    def array(self):
        return self.__array
    
    @property
    def size(self):
        return self.__size
    
    @property
    def label(self):
        return self.__label
    
    @property
    def zero(self):
        return self.__zero
    
    def __str__(self):
        return ...