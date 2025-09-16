def get_bioavail_factor(metal, pH, crop=None):
    """
    Simulate bioavailability of heavy metals based on pH and crop.
    Simplified rules mimicking speciation/precipitation (e.g., Cd precipitates at high pH).
    Returns factor (0-1) adjusting metal availability for plant uptake.
    """
    if metal == 'Cd':
        return 0.5 if pH > 7 else 0.8
    elif metal == 'As':
        if crop in ['Rice', 'Spinach']:  # Higher for As-sensitive crops
            return 0.9 if pH < 7 else 0.5
        return 0.7 if pH < 7 else 0.4
    elif metal == 'Pb':
        return 0.3 if pH > 7 else 0.6
    elif metal == 'Zn':
        return 0.9  # Less pH-sensitive
    elif metal == 'Cr':
        return 0.5 if pH > 7 else 0.8
    elif metal == 'Cu':
        return 0.6
    else:
        return 0.5  # Default for unlisted metals