class Stuhl:
    anzahl_rollen: int
    maximale_hoehe: float
    niedrigste_hoehe: float
    maximale_fuß_lehne: float
    niedrigste_fuß_lehne: float
    anzahl_der_lehnen: int
    aktuelle_hoehe: float
    anzahl_der_hebel: float
    anzahl_fuß_lehne: int
    aktuelle_fuß_lehne_hoehe: float
    farbe: str
    marke: str

    def fahre_hoch(self):
        self.aktuelle_hoehe = self.maximale_hoehe

    def fahre_runter(self):
        self.aktuelle_hoehe = self.niedrigste_hoehe

    def fuß_lehne_ausfahren(self):
        self.aktuelle_fuß_lehne_hoehe = self.maximale_fuß_lehne

    def fuß_lehne_einfahren(self):
        self.aktuelle_fuß_lehne_hoehe = self.niedrigste_fuß_lehne

    def __str__(self):
        return f'Stuhl der marke {self.marke}'
        
    # Wenn ich von 2 Leuten den Stul printe und + mache gibt er 'Unfall' zurück
    def __add__(self):
        return 'Unfall'

    def __init__(self, anzahl_rollen, maximale_hoehe, niedrigste_hoehe, maximale_fuß_lehne, niedrigste_fuß_lehne, anzahl_der_lehnen, aktuelle_hoehe, anzahl_der_hebel,
     anzahl_fuß_lehne, aktuelle_fuß_lehne_hoehe, farbe, marke ) -> None:

        self.anzahl_rollen = anzahl_rollen
        self.maximale_hoehe = maximale_hoehe
        self.niedrigste_hoehe = niedrigste_hoehe
        self.maximale_fuß_lehne = maximale_fuß_lehne
        self.niedrigste_fuß_lehne = niedrigste_fuß_lehne
        self.anzahl_der_lehnen = anzahl_der_lehnen
        self.aktuelle_hoehe = aktuelle_hoehe
        self.anzahl_der_hebel = anzahl_der_hebel
        self.anzahl_fuß_lehne = anzahl_fuß_lehne
        self.aktuelle_fuß_lehne_hoehe = aktuelle_fuß_lehne_hoehe
        self.farbe = farbe
        self.marke = marke

#########################################################################################################################################################################

gamer_stuhl_von_Kevin = Stuhl(anzahl_rollen = 5, maximale_hoehe = 1.5, niedrigste_hoehe = 1.3, maximale_fuß_lehne = 0.5, niedrigste_fuß_lehne = 0, anzahl_der_lehnen = 3,
 aktuelle_hoehe = 1.4, anzahl_der_hebel = 2, anzahl_fuß_lehne = 1, aktuelle_fuß_lehne_hoehe = 0.3, farbe = 'Schwartz und Rot', marke = 'No name Marke'  )

print(gamer_stuhl_von_Kevin)