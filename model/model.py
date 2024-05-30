import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi = []
        self._grafo = nx.Graph()
        self.idMApRetailer = {}

    def getAllCountries(self):
        countries = DAO.getCountry()
        return countries

    def buildGraph(self, country,anno):
        self._grafo.clear()
        self._nodi = DAO.getRetailersOfCountry(country)
        self._grafo.add_nodes_from(self._nodi)

        self.idMApRetailer = {}
        for r in self._nodi:
            self.idMApRetailer[r.Retailer_code] = r

        self.creaArchi(anno)

    def creaArchi(self,anno):
        self._grafo.clear_edges()
        for u in self._nodi:
            for v in self._nodi:
                if u!= v:
                    peso = DAO.getPesoRetailers(anno,u.Retailer_code,v.Retailer_code)
                    if peso[0] >0:
                        self._grafo.add_edge(u,v, weight=peso[0])


    def volumeRetailers(self):
        listaPesi = []
        for u in self._nodi:
            peso = 0
            vicini = self._grafo.neighbors(u)
            for v in vicini:
                peso += self._grafo[u][v]["weight"]
            if peso >0:
                listaPesi.append((u,peso))
        return listaPesi




    def printGraphDetails(self):
        return (f"Grafo creato con {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi.")