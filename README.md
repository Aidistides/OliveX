# OliveX
Measuring Olive Oil Polyphenols

Measure the remaining polyphenol content (in mg/kg gallic acid equivalents) in olive oil at the time of bottling, based on the elapsed time since pressing/extraction.

# OlivePolyPredictor

**AI model to predict polyphenol content in EVOO at bottling time based on time since pressing.**

Polyphenols degrade post-pressing. This tool helps producers, millers, and quality teams estimate remaining levels *before* bottling — without waiting for expensive lab tests.

## Science Background
- Polyphenols follow pseudo-first-order degradation (studies: e.g., 18-month storage trials at 5–50°C).
- Key factors: time, temperature (Arrhenius-like acceleration), light, oxygen.
- Example losses: ~30–40% in 3–6 months at room temp; far less in cool/dark storage.
- Typical fresh EVOO: 200–1500+ mg/kg (varies by cultivar, harvest timing).

## Features
- Inputs: initial polyphenols (optional estimate), days since pressing, avg. temp (°C), light/oxygen exposure flags.
- Output: predicted polyphenols (mg/kg) at bottling + confidence interval.
- Baseline comparison: pure exponential decay model.
- Trained on 1,000+ synthetic samples calibrated to real degradation data.

## Installation
```bash
git clone https://github.com/yourusername/olive_oil_polyphenol_predictor.git
cd olive_oil_polyphenol_predictor
pip install -r requirements.txt
