import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        anni = [2015,2016,2017,2018]
        for year in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(year))
        nazioni = self._model.getAllCountries()
        for country in nazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(country))

        self._view.update_page()


    def handle_graph(self, e):
        year = self._view.ddyear.value
        country = self._view.ddcountry.value
        self._model.buildGraph(country,year)

        dati = self._model.printGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(dati))
        self._view.btn_volume.disabled = False

        self._view.update_page()



    def handle_volume(self, e):
        listaPesi = sorted(self._model.volumeRetailers(), key=lambda x: x[1], reverse=True)
        self._view.txtOut2.controls.clear()
        for p in listaPesi:
            self._view.txtOut2.controls.append(ft.Text(f"{p[0].Retailer_name} ----> {p[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
