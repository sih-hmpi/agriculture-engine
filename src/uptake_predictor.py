from reaction_simulator import get_bioavail_factor

def predict_uptake(row, conc, pH):
    """
    Predict heavy metal uptake (mg/kg) for a crop-metal pair.
    Inputs: DataFrame row (crop, metal, bcf, threshold), concentration (mg/L), pH.
    Returns: Predicted uptake in crop (mg/kg).
    """
    bio_factor = get_bioavail_factor(row['metal'], pH, row['crop'])
    return row['bcf'] * conc * bio_factor