# ============================================================================================
# SEZIONE 1: Importazioni
# ============================================================================================


# ============================================================================================
# SEZIONE 2: Classi
# ============================================================================================
class Punto:
    """Rappresenta un punto nello spazio tridimensionale.

    Attributi:
        posizione (list): Una lista di tre valori che rappresentano le coordinate x, y e z del punto nello spazio.

    Esempio:
        >>> punto = Punto([1.0, 2.0, 3.0])
        >>> print(punto.posizione)
        [1.0, 2.0, 3.0]
    """
    def __init__(self, posizione: list):
        """Inizializza un'istanza di Punto con una posizione specificata.

        Args:
            posizione (list): Una lista di tre valori che rappresentano le coordinate x, y e z del punto.
        """
        self.posizione = posizione
    
    def posizione(self):
        '''Visualizza e restituisce i valori di posizione.

        Parametri:
            L'oggetto Punto istanziato.

        Valore di ritorno:
            Il valore di posizione (list).

        Esempio:
        >>> punto = Punto([5, 6, 8])
        >>> pos = punto.posizione()
        >>> Posizione: [5, 6, 8]
        >>> print(pos)
        >>> [5, 6, 8]
        '''
        return self.posizione

class Corpo:
    """Rappresenta un corpo carico nello spazio tridimensionale.

    Attributi:
        posizione (list): Una lista di tre valori che rappresentano le coordinate x, y e z del corpo nello spazio.
        carica (float): Il valore della carica del corpo in Coulomb.

    Esempio:
        >>> corpo = Corpo([1.0, 2.0, 3.0], 1e-6)
        >>> print(corpo.posizione)
        [1.0, 2.0, 3.0]
        >>> print(corpo.carica)
        1e-6
    """
    def __init__(self, posizione: list, carica: float):
        """Inizializza un'istanza di Corpo con una posizione specificata e una carica.

        Args:
            posizione (list): Una lista di tre valori che rappresentano le coordinate x, y e z del corpo.
            carica (float): Il valore della carica del corpo in Coulomb.
        """
        self.posizione = posizione
        self.carica = carica

# ============================================================================================
# SEZIONE 3: Funzioni
# ============================================================================================


