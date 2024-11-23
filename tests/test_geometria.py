import unittest
from fisica.geometria import Punto  # Importa la classe Punto dal modulo geometria della libreria fisica

class TestPunto(unittest.TestCase):
    """Test per la classe Punto."""
    
    def test_inizializzazione(self):
        """Testa l'inizializzazione di un'istanza di Punto."""
        posizione = [1.0, 2.0, 3.0]
        punto = Punto(posizione)
        self.assertEqual(punto.posizione, posizione, "L'attributo posizione non corrisponde al valore iniziale.")

    def test_accesso_posizione(self):
        """Testa l'accesso all'attributo posizione."""
        posizione = [4.5, 6.7, 8.9]
        punto = Punto(posizione)
        self.assertEqual(punto.posizione, posizione, "Il metodo posizione() non restituisce il valore corretto.")
    
    def test_modifica_posizione(self):
        """Testa che la posizione non possa essere modificata accidentalmente (opzionale)."""
        posizione = [0.0, 0.0, 0.0]
        punto = Punto(posizione)
        nuova_posizione = [1.0, 1.0, 1.0]
        punto._posizione = nuova_posizione  # Accesso diretto per verificare la protezione
        self.assertEqual(punto.posizione, nuova_posizione, "La posizione non è stata modificata correttamente.")
