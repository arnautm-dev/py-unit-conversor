#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Configurar encoding per a la terminal Windows
if os.name == 'nt':
    sys.stdout.reconfigure(encoding='utf-8')

# Colors ANSI per a la terminal
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def disable():
        Colors.HEADER = ''
        Colors.OKBLUE = ''
        Colors.OKCYAN = ''
        Colors.OKGREEN = ''
        Colors.WARNING = ''
        Colors.FAIL = ''
        Colors.ENDC = ''
        Colors.BOLD = ''
        Colors.UNDERLINE = ''

# Factors de conversió respecte a la unitat base
UNITATS = {
    "Llargada": {
        "nanoímetres (nm)": 1e-9,
        "microímetres (μm)": 1e-6,
        "mil·límetres (mm)": 0.001,
        "centímetres (cm)": 0.01,
        "decímetres (dm)": 0.1,
        "metres (m)": 1,
        "decàmetres (dam)": 10,
        "hectòmetres (hm)": 100,
        "quilòmetres (km)": 1000,
        "polzades (in)": 0.0254,
        "peus (ft)": 0.3048,
        "iardes (yd)": 0.9144,
        "milles terrestres": 1609.344,
        "milles marines": 1852,
        "angstroms (Å)": 1e-10,
    },
    "Massa": {
        "micrograms (μg)": 1e-6,
        "mil·ligrams (mg)": 0.001,
        "centigrams (cg)": 0.01,
        "decigrams (dg)": 0.1,
        "grams (g)": 1,
        "decagrams (dag)": 10,
        "hectograms (hg)": 100,
        "quilograms (kg)": 1000,
        "tones mètriques (t)": 1_000_000,
        "onzes (oz)": 28.3495,
        "lliures (lb)": 453.592,
        "pedres (st)": 6350.29,
        "quilates (ct)": 0.0002,
        "tonelades (tn)": 1_000_000,
    },
    "Capacitat": {
        "mil·lilitres (mL)": 0.001,
        "centilitres (cL)": 0.01,
        "decilitres (dL)": 0.1,
        "litres (L)": 1,
        "decalitres (daL)": 10,
        "hectolitres (hL)": 100,
        "quilolitres (kL)": 1000,
        "culleretes (tsp)": 0.00492892,
        "cullerades (tbsp)": 0.0147868,
        "galons USA (gal US)": 3.78541,
        "galons imperials (gal imp)": 4.54609,
        "barils USA": 158.987,
        "pints (pt)": 0.473176,
        "quarts (qt)": 0.946353,
        "tasses (cup)": 0.236588,
    },
    "Volum": {
        "mil·límetres cúbics (mm³)": 1e-9,
        "centímetres cúbics (cm³)": 1e-6,
        "decímetres cúbics (dm³)": 0.001,
        "metres cúbics (m³)": 1,
        "quilòmetres cúbics (km³)": 1e9,
        "polzades cúbiques (in³)": 0.0000163871,
        "peus cúbics (ft³)": 0.0283168,
        "iardes cúbiques (yd³)": 0.764555,
        "milles cúbiques": 4.168e9,
    },
    "Temps": {
        "nanosegons (ns)": 1e-9,
        "microsegons (μs)": 1e-6,
        "mil·lisegons (ms)": 0.001,
        "centisegons (cs)": 0.01,
        "decisegons (ds)": 0.1,
        "segons (s)": 1,
        "minuts (min)": 60,
        "hores (h)": 3600,
        "dies (d)": 86400,
        "setmanes (w)": 604800,
        "mesos (aprox)": 2_592_000,
        "anys (aprox)": 31_536_000,
        "dècades (aprox)": 315_360_000,
        "segles (aprox)": 3_153_600_000,
    },
    "Temperatura": {
        "Celsius (°C)": "special",
        "Fahrenheit (°F)": "special",
        "Kelvin (K)": "special",
    },
    "Pressió": {
        "pascals (Pa)": 1,
        "hectopascals (hPa)": 100,
        "kilopascals (kPa)": 1000,
        "megapascals (MPa)": 1_000_000,
        "bars (bar)": 100_000,
        "atmosferes (atm)": 101_325,
        "mm de mercuri (mmHg)": 133.322,
        "psi (psi)": 6894.76,
        "torr": 133.322,
    },
    "Energia": {
        "joules (J)": 1,
        "quilojoules (kJ)": 1000,
        "megajoules (MJ)": 1_000_000,
        "gigajoules (GJ)": 1_000_000_000,
        "calories (cal)": 4.184,
        "kilocalories (kcal)": 4184,
        "watt-hora (Wh)": 3600,
        "kilowatt-hora (kWh)": 3_600_000,
        "electron-volts (eV)": 1.60218e-19,
        "BTU": 1055.06,
        "ergs": 1e-7,
    },
    "Velocitat": {
        "metres per segon (m/s)": 1,
        "quilòmetres per hora (km/h)": 0.277778,
        "milles per hora (mph)": 0.44704,
        "nusos (kn)": 0.51444,
        "peus per segon (ft/s)": 0.3048,
        "pedes per hora": 0.000084667,
    },
    "Àrea": {
        "mil·límetres quadrats (mm²)": 1e-6,
        "centímetres quadrats (cm²)": 1e-4,
        "metres quadrats (m²)": 1,
        "quilòmetres quadrats (km²)": 1_000_000,
        "hectàrees (ha)": 10_000,
        "àrees (a)": 100,
        "polzades quadrades (in²)": 0.00064516,
        "peus quadrats (ft²)": 0.092903,
        "iardes quadrades (yd²)": 0.836127,
        "milles quadrades": 2_589_988,
        "acres": 4046.86,
    },
    "Densitat": {
        "kg/m³": 1,
        "g/cm³": 1000,
        "g/mL": 1000,
        "lb/ft³": 16.0185,
        "lb/in³": 27679.9,
        "oz/in³": 1729.99,
    },
}

def convertir_temperatura(valor, origen, desti):
    """Converteix temperatures entre Celsius, Fahrenheit i Kelvin"""
    try:
        valor = float(valor)
        
        # Primer convertim a Celsius (unitat base)
        if origen == "Celsius (°C)":
            celsius = valor
        elif origen == "Fahrenheit (°F)":
            celsius = (valor - 32) * 5/9
        elif origen == "Kelvin (K)":
            celsius = valor - 273.15
        
        # Depois convertim de Celsius a la unitat destí
        if desti == "Celsius (°C)":
            resultat = celsius
        elif desti == "Fahrenheit (°F)":
            resultat = celsius * 9/5 + 32
        elif desti == "Kelvin (K)":
            resultat = celsius + 273.15
        
        return resultat
    except ValueError:
        return None

def convertir_unitats(valor, origen, desti, tipus):
    """Converteix entre unitats"""
    try:
        valor = float(valor)
        
        if tipus == "Temperatura":
            return convertir_temperatura(valor, origen, desti)
        
        # Conversió normal
        factor_origen = UNITATS[tipus][origen]
        factor_desti = UNITATS[tipus][desti]
        
        # Convertim a unitat base i depois a la destí
        valor_base = valor * factor_origen
        resultat = valor_base / factor_desti
        
        return resultat
    except (ValueError, KeyError):
        return None

def mostrar_capçalera():
    """Mostra la capçalera del programa"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Colors.HEADER}{Colors.BOLD}")
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║          🔄 CONVERSOR D'UNITATS - v2.0                    ║")
    print("║     Conversió ràpida i fàcil de totes les unitats         ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print(f"{Colors.ENDC}\n")

def mostrar_menu_principal():
    """Mostra el menú principal amb els tipus d'unitats disponibles"""
    print(f"{Colors.OKBLUE}{Colors.BOLD}═══════════════════════════════════════════════════════════{Colors.ENDC}")
    print(f"{Colors.BOLD}  Selecciona el tipus d'unitat que vols convertir:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}═══════════════════════════════════════════════════════════{Colors.ENDC}\n")
    
    tipus_list = list(UNITATS.keys())
    for i, tipus in enumerate(tipus_list, 1):
        emoji_map = {
            "Llargada": "📏",
            "Massa": "⚖️ ",
            "Capacitat": "🥛",
            "Volum": "📦",
            "Temps": "⏱️ ",
            "Temperatura": "🌡️ ",
            "Pressió": "🔧",
            "Energia": "⚡",
            "Velocitat": "🚀",
            "Àrea": "📐",
            "Densitat": "🧪",
        }
        emoji = emoji_map.get(tipus, "🔢")
        print(f"  {Colors.OKGREEN}{i:2d}{Colors.ENDC} - {emoji} {Colors.BOLD}{tipus}{Colors.ENDC}")
    
    print(f"  {Colors.WARNING}0{Colors.ENDC}  - {Colors.BOLD}Sortir{Colors.ENDC}\n")

def mostrar_unitats(tipus):
    """Mostra les unitats disponibles per un tipus"""
    unitats = UNITATS[tipus]
    print(f"\n{Colors.BOLD}{Colors.OKBLUE}Unitats de {tipus}:{Colors.ENDC}\n")
    for i, unitat in enumerate(unitats.keys(), 1):
        print(f"  {Colors.OKGREEN}{i:2d}{Colors.ENDC} - {unitat}")
    print()

def seleccionar_unitat(tipus):
    """Permet seleccionar una unitat d'un tipus"""
    unitats_list = list(UNITATS[tipus].keys())
    while True:
        try:
            num = int(input(f"{Colors.BOLD}Selecciona el número de l'opció: {Colors.ENDC}"))
            if 1 <= num <= len(unitats_list):
                return unitats_list[num - 1]
            else:
                print(f"{Colors.FAIL}Número inválid. Torna a intentar.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Introdueix un número vàlid.{Colors.ENDC}")

def obtenir_valor():
    """Demana a l'usuari que introdueixi un valor"""
    while True:
        try:
            valor = input(f"{Colors.BOLD}Introdueix el valor a convertir: {Colors.ENDC}")
            return float(valor)
        except ValueError:
            print(f"{Colors.FAIL}Valor inválid. Introdueix un número.{Colors.ENDC}")

def mostrar_resultat(valor_original, unitat_origen, valor_final, unitat_destí):
    """Mostra el resultat de la conversió de forma elegantament"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}╔════════════════════════════════════════════════════════╗{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}║                    RESULTAT DE LA CONVERSIÓ            ║{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}╚════════════════════════════════════════════════════════╝{Colors.ENDC}")
    print(f"\n  {Colors.OKGREEN}{Colors.BOLD}{valor_original:.6g}{Colors.ENDC} {Colors.OKCYAN}{unitat_origen}{Colors.ENDC}")
    print(f"  {Colors.WARNING}⟹{Colors.ENDC}")
    print(f"  {Colors.OKGREEN}{Colors.BOLD}{valor_final:.6g}{Colors.ENDC} {Colors.OKCYAN}{unitat_destí}{Colors.ENDC}\n")

def processar_conversio(tipus):
    """Processa la conversió d'unitats"""
    # Mostrar unitats disponibles i seleccionar origen
    mostrar_unitats(tipus)
    print(f"{Colors.BOLD}Selecciona l'unitat d'ORIGEN:{Colors.ENDC}")
    unitat_origen = seleccionar_unitat(tipus)
    
    # Seleccionar destí
    print(f"\n{Colors.BOLD}Selecciona l'unitat de DESTÍ:{Colors.ENDC}")
    mostrar_unitats(tipus)
    unitat_destí = seleccionar_unitat(tipus)
    
    # Obtenir valor
    valor = obtenir_valor()
    
    # Convertir
    resultat = convertir_unitats(valor, unitat_origen, unitat_destí, tipus)
    
    if resultat is not None:
        mostrar_resultat(valor, unitat_origen, resultat, unitat_destí)
    else:
        print(f"{Colors.FAIL}Error en la conversió. Torna a intentar.{Colors.ENDC}\n")

def programa_principal():
    """Funció principal del programa"""
    while True:
        mostrar_capçalera()
        mostrar_menu_principal()
        
        try:
            opcio = int(input(f"{Colors.BOLD}Introdueix el número de l'opció: {Colors.ENDC}"))
            
            if opcio == 0:
                print(f"\n{Colors.OKGREEN}{Colors.BOLD}Fins aviat! 👋{Colors.ENDC}\n")
                break
            
            tipus_list = list(UNITATS.keys())
            if 1 <= opcio <= len(tipus_list):
                tipus_seleccionat = tipus_list[opcio - 1]
                processar_conversio(tipus_seleccionat)
                input(f"\n{Colors.WARNING}Prem INTRO per continuar...{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}Opció inválida. Torna a intentar.{Colors.ENDC}")
                input(f"\n{Colors.WARNING}Prem INTRO per continuar...{Colors.ENDC}")
        
        except ValueError:
            print(f"{Colors.FAIL}Introdueix un número vàlid.{Colors.ENDC}")
            input(f"\n{Colors.WARNING}Prem INTRO per continuar...{Colors.ENDC}")

# Punt d'entrada del programa
if __name__ == "__main__":
    programa_principal()
