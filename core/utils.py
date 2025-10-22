import numpy as np

class Utils:
    """Utils class: a collection of methods to manipulate the set morphism of the simplicial category and the matrix representation under the canonical morphism to vector spaces.
    
    Attributes
    -------
    basic_vector:

    matrix_morphism:

    valid_mapping:
    """
    
    def basic_vector(index:int, dimension:int):
        vec = np.zeros(dimension)
        vec[index] = 1
        return vec

    def matrix_morphism(domain : int, codomain: int, mapping: np.array):
        matrix = np.zeros((codomain, domain), dtype=np.int64)
        matrix[mapping, range(domain)] = 1
        return matrix

    def valid_mapping(domain:int, codomain: int, mapping: np.array):
        def isOrderPreserving(mapping):
            return  np.all(mapping == np.sort(mapping))

        def wellDefined(domain, codmain, mapping):
            return np.all(mapping <= codmain) and (mapping.shape[0] == domain) 
    
        return isOrderPreserving(mapping) and wellDefined(domain, codomain, mapping)
    
    