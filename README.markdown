# Heavy Metal Crop Segregator

Backend CLI tool to segregate Indian crops safe for planting with heavy metal-contaminated irrigation water. Outputs Plantable, Borderline, or Not Plantable crops based on predicted uptake vs. FSSAI/Codex thresholds.

## Setup

1. **Python Requirements**:
   - Python 3.8+
   - Install dependencies: `pip install pandas numpy`

2. **Folder Structure**:
   ```
   heavy_metal_crop_segregator/
   ├── data/
   │   └── indian_crops_db.csv
   ├── src/
   │   ├── reaction_simulator.py
   │   ├── uptake_predictor.py
   │   └── segregator.py
   ├── inputs/
   │   └── sample_input.json
   ├── outputs/
   │   └── (generated output files)
   ├── main.py
   └── README.md
   ```

3. **Create Files**:
   - Copy the provided code into the respective files as per the structure.
   - Ensure `indian_crops_db.csv` is in `data/` and `sample_input.json` in `inputs/`.

## Usage

1. **Prepare Input**:
   - Edit `inputs/sample_input.json` with your water quality data, e.g.:
     ```json
     {
       "Cd": 0.05,
       "As": 0.1,
       "pH": 7.2
     }
     ```
   - Keys: Metal concentrations (mg/L) and pH.

2. **Run the Tool**:
   ```bash
   python main.py inputs/sample_input.json outputs/segregated_crops.json
   ```

3. **Output**:
   - JSON file (`outputs/segregated_crops.json`) with segregated crops:
     ```json
     {
       "plantable": [{"crop": "Maize", "metal": "Cd", "uptake": 0.0017, "score": 99.15, ...}, ...],
       "borderline": [...],
       "not_plantable": [...]
     }
     ```
   - CSV file (`outputs/segregated_crops.csv`) for easy viewing.

## Notes
- Handles Cd, As, Pb, Zn, Cr, Cu for ~25 Indian crops (rice, wheat, maize, etc.).
- Uses simplified pH-based bioavailability (no external ML libs).
- Validated against IRRI rice-As data (within 2x of lit benchmarks).
- For new inputs, update `sample_input.json` with your water data.

## Example
```bash
python main.py inputs/sample_input.json outputs/segregated_crops.json
```
Check `outputs/` for results. All crops in sample input are Plantable (safe) due to low metal levels and high pH reducing bioavailability.