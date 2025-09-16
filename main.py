import pandas as pd
import json
import os
import sys
# Add src/ to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from segregator import segregate_crops

def main(input_file, output_file):
    # Load crop database
    df = pd.read_csv('data/indian_crops_db.csv')
    
    # Load input water quality data
    with open(input_file, 'r') as f:
        input_data = json.load(f)
    
    # Extract pH and metal concentrations
    pH = input_data.get('pH', 7.0)
    metal_conc_dict = {k: v for k, v in input_data.items() if k != 'pH'}
    
    # Run segregation
    segregated = segregate_crops(df, metal_conc_dict, pH)
    
    # Save output
    os.makedirs('outputs', exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(segregated, f, indent=2)
    
    # Also save as CSV for convenience
    csv_data = []
    for category, items in segregated.items():
        for item in items:
            item['category'] = category
            csv_data.append(item)
    pd.DataFrame(csv_data).to_csv(output_file.replace('.json', '.csv'), index=False)
    
    print(f"Results saved to {output_file} and {output_file.replace('.json', '.csv')}")

if __name__ == '__main__':
    main('inputs/my_input.json', 'outputs/my_results.json')