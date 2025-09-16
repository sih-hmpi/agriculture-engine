from uptake_predictor import predict_uptake
from reaction_simulator import get_bioavail_factor

def segregate_crops(df, metal_conc_dict, pH):
    """
    Segregate crops based on predicted uptake vs. safety thresholds.
    Inputs: DataFrame (crop DB), metal_conc_dict (e.g., {'As': 0.15}), pH.
    Returns: Dict with 'plantable', 'borderline', 'not_plantable' lists.
    """
    results = []
    for idx, row in df.iterrows():
        if row['metal'] in metal_conc_dict:
            conc = metal_conc_dict[row['metal']]
            uptake = predict_uptake(row, conc, pH)
            threshold = row['threshold']
            score = ((threshold - uptake) / threshold) * 100 if uptake < threshold else 0
            category = 'Plantable' if score > 40 else 'Borderline' if score > 10 else 'Not Plantable'
            results.append({
                'crop': row['crop'],
                'metal': row['metal'],
                'uptake': round(uptake, 4),
                'score': round(score, 2),
                'category': category,
                'reason': f"Bioavail factor: {get_bioavail_factor(row['metal'], pH, row['crop']):.2f}"
            })
    segregated = {
        'plantable': sorted([r for r in results if r['category'] == 'Plantable'], key=lambda x: x['score'], reverse=True),
        'borderline': sorted([r for r in results if r['category'] == 'Borderline'], key=lambda x: x['score'], reverse=True),
        'not_plantable': sorted([r for r in results if r['category'] == 'Not Plantable'], key=lambda x: x['score'], reverse=True)
    }
    return segregated