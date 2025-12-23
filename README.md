# 🔄 CONVERSOR D'UNITATS

## Descripció

Un conversor d'unitats complet i visual, creat en Python, que permet convertir entre moltes unitats de mesura en català.

---

## 📋 Tipus d'Unitats Disponibles

### 1. **Llargada** (📏)
- Unitats mètriques: nanoímetres, microímetres, mil·límetres, centímetres, metres, quilòmetres, etc.
- Unitats anglosaxones: polzades, peus, iardes, milles terrestres i marines
- 15 unitats disponibles

### 2. **Massa** (⚖️)
- Unitats mètriques: grams, quilograms, tones, etc.
- Unitats anglosaxones: onzes, lliures, pedres
- 14 unitats disponibles

### 3. **Capacitat** (🥛)
- Unitats mètriques: mil·lilitres, litres, hectolitres, etc.
- Unitats de cuina: culleretes, cullerades, tasses
- Unitats anglosaxones: galons USA i imperials
- 15 unitats disponibles

### 4. **Volum** (📦)
- Unitats cúbiques mètriques i anglosaxones
- 9 unitats disponibles

### 5. **Temps** (⏱️)
- Des de nanosegons fins a segles
- Unitats aprox. per períodes llargs
- 14 unitats disponibles

### 6. **Temperatura** (🌡️)
- Celsius, Fahrenheit, Kelvin
- Conversió especial amb fórmules matemàtiques

### 7. **Pressió** (🔧)
- Pascals, bars, atmosferes, psi, torr, etc.
- 9 unitats disponibles

### 8. **Energia** (⚡)
- Joules, caloríes, watts-hora, BTU, electron-volts
- 11 unitats disponibles

### 9. **Velocitat** (🚀)
- m/s, km/h, mph, nusos, peus/s
- 6 unitats disponibles

### 10. **Àrea** (📐)
- Metre quadrat, quilòmetre quadrat, hectàrees, acres, etc.
- 11 unitats disponibles

### 11. **Densitat** (🧪)
- kg/m³, g/cm³, lb/ft³, etc.
- 6 unitats disponibles

---

## 🚀 Com Executar el Programa

### Opció 1: Executar directament
```bash
python conversor-unitats.py
```

### Opció 2: Des de PowerShell
```powershell
cd "C:\Users\Usuari\Documents\unit-conversor"
python conversor-unitats.py
```

---

## 📖 Com Utilitzar

1. **Seleccionar categoria**: Escriu el número del tipus d'unitat (1-11)
2. **Seleccionar unitat d'origen**: Escriu el número de la unitat que tens
3. **Seleccionar unitat de destí**: Escriu el número de la unitat que vols
4. **Introduir valor**: Escriu la quantitat a convertir
5. **Veure resultat**: El programa mostrarà la conversió

### Exemple
```
Selecciona el número de l'opció: 1           [Triem Llargada]
Selecciona l'unitat d'ORIGEN: 6              [metres]
Selecciona l'unitat de DESTÍ: 9              [quilòmetres]
Introdueix el valor a convertir: 5000        [5000 metres]
Resultat: 5 km
```

---

## 🎨 Característiques Visuals

- **Colors ANSI**: Menús colorits i fàcils de llegir
- **Emojis**: Identificació ràpida de tipus d'unitats
- **Caixes de text**: Separació clara entre seccions
- **Formatat**: Números ben presentats amb precisió

---

## 💻 Requisits

- Python 3.6+
- Windows, macOS o Linux

---

## 🔧 Funcionalitats Tècniques

- **Factors de conversió**: Base unitaria per a cada categoria
- **Temperatura especial**: Conversió mitjançant fórmules matemàtiques
- **Validació d'entrada**: Comprova números vàlids
- **Interfície robusta**: Maneja errors graciosament
- **En català**: Tot el programa està en català

---

## 📝 Estructura del Codi

```
conversor-unitats.py
├── Classes
│   └── Colors (per a colors ANSI)
├── Diccionaris
│   └── UNITATS (totes les conversions)
├── Funcions de Conversió
│   ├── convertir_temperatura()
│   ├── convertir_unitats()
├── Funcions de Visualització
│   ├── mostrar_capçalera()
│   ├── mostrar_menu_principal()
│   ├── mostrar_unitats()
│   ├── mostrar_resultat()
└── Funció Principal
    └── programa_principal()
```

---

## 🔐 Seguretat i Validació

- Validació de números (comprovació de ValueError)
- Selecció d'unitats amb índexs (sense input de strings)
- Manejo d'excepcions per a casos d'error

---

## 📚 Exemples de Conversió

| Origen | Valor | Destí | Resultat |
|--------|-------|-------|----------|
| metres | 100 | quilòmetres | 0.1 km |
| grams | 1000 | quilograms | 1 kg |
| litres | 1 | mil·lilitres | 1000 mL |
| Celsius | 25 | Fahrenheit | 77°F |
| hores | 2 | segons | 7200 s |

---

## 👨‍💻 Autor

[ArnauTM-dev](https://arnautm-dev.netlify.app)

[arnautm-dev@proton.me](mailto:arnautm-dev@proton.me)

---

**Gaudeix del conversor!** 🎉
