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

def esegui_protocollo(num_iterazioni=5):
    """
    Esegue il protocollo di routing per un massimo di num_iterazioni.
    Si ferma anticipatamente se non ci sono più cambiamenti.
    """
    for iterazione in range(num_iterazioni):
        print(f"\nIterazione {iterazione + 1}:")
        cambiamenti = any(aggiorna_tabella(nodo) for nodo in rete)
        if not cambiamenti:  # Se non ci sono stati cambiamenti, interrompe il ciclo
            print("Convergenza raggiunta!")
            break
        mostra_tabelle_routing(intermedio=True)


def mostra_tabelle_routing(intermedio=False):
    """
    Stampa le tabelle di routing in formato leggibile per ciascun nodo.
    """
    titolo = "Tabelle di routing intermedie" if intermedio else "Tabelle di routing finali"
    print(f"\n{titolo}:\n")
    for nodo, tabella in tabelle_routing.items():
        dati = [
            [destinazione, costo, next_hop if next_hop is not None else "None"]
            for destinazione, (costo, next_hop) in tabella.items()
        ]
        print(f"Tabella di Routing per {nodo}:")
        print(tabulate(dati, headers=["Destinazione", "Costo", "Next Hop"], tablefmt="grid"))
        print()


# Esecuzione del protocollo di routing
if __name__ == "__main__":
    print("Esecuzione del protocollo Distance Vector...")
    esegui_protocollo(num_iterazioni=5)
    mostra_tabelle_routing()