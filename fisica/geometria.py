# ============================================================================================
# SEZIONE 1: Importazioni
# ============================================================================================

from scipy import constants as cns
from math import sqrt, atan2, cos, sin, pi, prod

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
        self._posizione = posizione
    
    @property
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
        return self._posizione
    
    def distanza(self, ente2):
        '''Distanza in coordinate cartesiane in uno spazio n-dimensionale

    Descrizione:
        La funzione prende le coordinate cartesiane di due punti e restituisce
        la distanza fra i due punti.

    Parametri:
        - self: istanza della classe Corpo o Punto
        - ente2: istanza della classe Corpo o Punto
    
    Valore di ritorno:
        - distanza float valore della distanza fra due corpi o punti
    
    Esempio:
        >>> corpo1:Punto = Punto([1,5,8], 1.59e-8)
        >>> corpo2:Corpo = Corpo([4,6,8], 1.22e-7)
        >>> distanza:float = corpo1.distanza(corpo2)
        >>> Distanza fra due corpi: 3.1622776601683795
    '''
        spostamento = [a - b for a, b in zip(self.posizione, ente2.posizione)]
        quadrato = [a ** 2 for a in spostamento]
        distanza = sqrt(sum(quadrato))
        return distanza
    
    def versore(self, ente2) -> tuple:
        '''Versore fra due punti in un spazion n-dimensionale

        Descrizione:
            Calcolo del versore fra due punti in uno spazio n-dimensionale

        Parametri:
            - ente1: istanza della classe Corpo o Punto
            - ente2: istanza della classe Corpo o Punto
        
        Valore di ritorno:
            - versore (tuple) fra due corpi o punti
        
        Esempio:
            >>> corpo1:Corpo = Corpo([1,5,8], 1.59e-8)
            >>> corpo2:Corpo = Corpo([4,6,8], 1.22e-7)
            >>> versore:tuple = calcolo_versore(corpo1, corpo2)
            >>> print(f"Versore: {versore}")
        '''
        spostamento = [a - b for a, b in zip(self.posizione, ente2.posizione)]
        distanza: float = self.distanza(ente2)
        versore = tuple([a / distanza for a in spostamento])
        return versore

class Corpo(Punto):
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
    def __init__(self, posizione: list = [0,0,0], massa:float = 0, carica: float = 0):
        """Inizializza un'istanza di Corpo con una posizione specificata e una carica.

        Args:
            posizione (list): Una lista di tre valori che rappresentano le coordinate x, y e z del corpo.
            carica (float): Il valore della carica del corpo in Coulomb.
        """
        super().__init__(posizione)
        self.carica = carica

# ============================================================================================
# SEZIONE 3: Funzioni
# ============================================================================================

def calcolo_distanza(ente1: Punto | Corpo, ente2: Punto | Corpo) -> float:
    '''Distanza in coordinate cartesiane in uno spazio n-dimensionale

    Descrizione:
        La funzione prende le coordinate cartesiane di due punti e restituisce
        la distanza fra i due punti.

    Parametri:
        - ente1: istanza della classe Corpo o Punto
        - ente2: istanza della classe Corpo o Punto
    
    Valore di ritorno:
        - distanza float valore della distanza fra due corpi o punti
    
    Esempio:
        >>> corpo1:Corpo = Corpo([1,5,8], 1.59e-8)
        >>> corpo2:Corpo = Corpo([4,6,8], 1.22e-7)
        >>> distanza:float = calcolo_distanza(corpo1, corpo2)
        >>> Distanza fra due corpi: 3.1622776601683795
    '''
    spostamento = [a - b for a, b in zip(ente1.posizione, ente2.posizione)]
    quadrato = [a ** 2 for a in spostamento]
    distanza = sqrt(sum(quadrato))
    return distanza

def calcolo_versore(ente1: Punto | Corpo, ente2: Punto | Corpo) -> tuple:
    '''Versore fra due punti in un spazion n-dimensionale

    Descrizione:
        Calcolo del versore fra due punti in uno spazio n-dimensionale

    Parametri:
        - ente1: istanza della classe Corpo o Punto
        - ente2: istanza della classe Corpo o Punto
    
    Valore di ritorno:
        - versore (tuple) fra due corpi o punti
    
    Esempio:
        >>> corpo1:Corpo = Corpo([1,5,8], 1.59e-8)
        >>> corpo2:Corpo = Corpo([4,6,8], 1.22e-7)
        >>> versore:tuple = calcolo_versore(corpo1, corpo2)
        >>> print(f"Versore: {versore}")
    '''
    spostamento = [a - b for a, b in zip(ente1.posizione, ente2.posizione)]
    distanza: float = calcolo_distanza(ente1, ente2)
    versore = tuple([a / distanza for a in spostamento])
    return versore

def cartesiane_polari(cart:list[float]) -> list[float]:
    '''Converte un insieme di coordinate cartesiane n-dimensionali in coordinate polari.

    Questa funzione accetta una lista di coordinate cartesiane e restituisce una lista 
    di coordinate polari. Il raggio `r` viene calcolato come la distanza dall'origine 
    e gli angoli sono calcolati iterativamente usando funzioni trigonometriche.

    Args:
        cart (list[float]): Una lista di float contenente le coordinate cartesiane.

    Returns:
        list[float]: Una lista di float contenente il raggio e `n-1` angoli polari.

    Example:
        >>> cartesiane_polari([3, 3, 3])
        >>> [5.196, 0.785, 0.615]

    Note:
        Gli angoli sono calcolati in ordine crescente rispetto agli assi cartesiani,
        e il raggio rappresenta la distanza euclidea dall'origine. 
    '''
    pol:list = []
    r:float = sqrt(sum([x**2 for x in cart]))
    pol.append(r) if r else pol
    i, n = 0, len(cart)
    while i < n-1:
        pol.append(atan2(cart[i], sqrt(sum([x**2 for x in cart[i+1:]]))))
        i += 1
    return pol

def polari_cartesiane(coordinate_polari:list[float]) -> list[float]:
    """Converte un insieme di coordinate polari n-dimensionali in coordinate cartesiane.

    Questa funzione accetta una lista di coordinate polari che includono il raggio `r` 
    e gli angoli di direzione. Utilizza iterativamente seno e coseno per calcolare 
    le coordinate cartesiane corrispondenti in uno spazio n-dimensionale.

    Args:
        coordinate_polari (list[float]): Una lista di float contenente il raggio `r`
        seguito da `n-1` angoli polari, in ordine.

    Returns:
        list[float]: Una lista di coordinate cartesiane corrispondenti, arrotondate a tre 
        cifre decimali.
    
    Example:
        >>> polari_cartesiane([3, 1.5708, 1.5708])
        >>> [0.0, 0.0, 3.0]

    Note:
        L'ordine degli angoli segue la convenzione delle coordinate polari 
        generalizzate, dove l'ultimo angolo determina la proiezione sull'asse 
        cartesiano principale, e gli altri angoli determinano le proiezioni 
        sugli assi rimanenti.
    """
    
    pol = coordinate_polari.copy()
    cartesiane = []
    r = pol[0]  # Estrai il raggio (il primo valore della lista)
    pol.pop(0)  # Rimuovi il raggio dalla lista
    pol.append(0)  # Aggiungi 0 alla fine per semplificare il calcolo finale

    while pol:
        coseno = float(cos(pol[-1]))  # Calcola il coseno dell'ultimo angolo
        pol.pop(-1)  # Rimuovi l'ultimo angolo dalla lista
        if pol:  # Se ci sono ancora angoli nella lista
            seni = [float(sin(x)) for x in pol]  # Calcola il seno di tutti gli angoli rimanenti
            produttoria = prod(seni)  # Moltiplica tutti i seni tra loro
            cartesiane.append(r * coseno * produttoria)  # Aggiungi il valore alla lista cartesiana
        else:
            cartesiane.append(r * coseno)  # Se non ci sono più angoli, aggiungi solo r*coseno

    return [round(coor,3) for coor in cartesiane]
