def get_bioavail_factor(metal, pH, crop=None):
    """
    Simulate bioavailability of heavy metals based on pH and crop.
    Simplified rules mimicking speciation/precipitation (e.g., Cd precipitates at high pH).
    Returns factor (0-1) adjusting metal availability for plant uptake.
    """
    # Priority/Regulated metals
    if metal == 'Cd':
        return 0.5 if pH > 7 else 0.8
    elif metal == 'As':
        if crop in ['Rice', 'Spinach']:  # Higher for As-sensitive crops
            return 0.9 if pH < 7 else 0.5
        return 0.7 if pH < 7 else 0.4
    elif metal == 'Pb':
        return 0.3 if pH > 7 else 0.6
    elif metal == 'Cr':
        return 0.5 if pH > 7 else 0.8
    elif metal == 'Hg':
        return 0.4 if pH > 7 else 0.7
    elif metal == 'Ni':
        return 0.5 if pH > 7 else 0.6
    elif metal == 'Cu':
        return 0.6
    elif metal == 'Zn':
        return 0.9
    elif metal == 'Fe':
        return 0.5 if pH > 7 else 0.7
    elif metal == 'Mn':
        return 0.6

    # Common/Frequently Monitored
    elif metal in ['Se', 'Al', 'B', 'Ba', 'Ag', 'Mo', 'Sb', 'Sn']:
        return 0.5 if pH > 7 else 0.7

    # Broader Trace Elements
    elif metal in ['Be', 'Sr', 'Li', 'Co', 'V', 'U', 'Th', 'Tl', 'Bi']:
        return 0.4 if pH > 7 else 0.6

    # Major Cations & Extended
    elif metal in ['Ca', 'Mg', 'Na', 'K']:
        return 0.3  # Essential, less bioavailable
    elif metal in ['Ga', 'Ge', 'Rb', 'In', 'Te', 'Cs', 'La', 'Ce', 'Nd', 'Sm']:
        return 0.4

    # Rare/Research Elements
    elif metal in ['Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Pd', 'Rh', 'Sc']:
        return 0.3  # Low bioavailability due to rarity

    else:
        return 0.5  # Default