import pandas as pd
import json
import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
# Add src/ to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from segregator import segregate_crops

# CLI function (unchanged)
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

# FastAPI setup
app = FastAPI(title="Heavy Metal Crop Segregator API")

# Pydantic model for input validation
class WaterQualityInput(BaseModel):
    pH: float
    metals: Dict[str, float]

# API endpoint for segregation
@app.post("/segregate")
async def segregate_crops_api(input_data: WaterQualityInput):
    df = pd.read_csv('data/indian_crops_db.csv')
    pH = input_data.pH
    metal_conc_dict = input_data.metals
    segregated = segregate_crops(df, metal_conc_dict, pH)
    return segregated

if __name__ == '__main__':
    # Run CLI if arguments provided, else start FastAPI server
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)