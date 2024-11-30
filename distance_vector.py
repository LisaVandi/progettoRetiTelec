"""
Implementazione di un protocollo di routing basato su Distance Vector.
"""
from tabulate import tabulate 

# Definizione della rete
rete = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

# Inizializzazione delle tabelle di routing per ciascun nodo
tabelle_routing = {
    nodo: {dest: (float('inf'), None) for dest in rete} for nodo in rete
}

# Ogni nodo conosce la distanza da sé stesso
for nodo in tabelle_routing:
    tabelle_routing[nodo][nodo] = (0, nodo)

def aggiorna_tabella(nodo):
    """
    Aggiorna la tabella di routing di un nodo con le informazioni ricevute dai vicini.
    Restituisce True se la tabella del nodo è stata aggiornata.
    """
    cambiato = False
    for vicino, costo_vicino in rete[nodo].items():
        for destinazione, (costo, _) in tabelle_routing[vicino].items():
            # Calcola il nuovo costo passando per il vicino
            nuovo_costo = costo_vicino + costo
            # Aggiorna solo se il nuovo costo è inferiore
            if nuovo_costo < tabelle_routing[nodo][destinazione][0]:
                print(f"Aggiornamento: {nodo} → {destinazione} via {vicino} (Nuovo costo: {nuovo_costo})")
                tabelle_routing[nodo][destinazione] = (nuovo_costo, vicino)
                cambiato = True
    return cambiato
