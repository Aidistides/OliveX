import argparse
from model.polyphenol_model import PolyphenolPredictor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict EVOO polyphenol content at bottling")
    parser.add_argument('--initial', type=float, required=True, help='Initial polyphenols (mg/kg)')
    parser.add_argument('--days', type=int, required=True, help='Days since pressing')
    parser.add_argument('--temp', type=float, default=18, help='Avg storage temp °C')
    parser.add_argument('--light', type=int, default=0, choices=[0,1], help='Light exposure (0/1)')
    parser.add_argument('--oxygen', type=int, default=0, choices=[0,1], help='Oxygen exposure (0/1)')
    
    args = parser.parse_args()
    
    predictor = PolyphenolPredictor()
    result = predictor.predict(args.initial, args.days, args.temp, args.light, args.oxygen)
    
    print(f"\n=== OlivePolyPredictor Results ===")
    print(f"Predicted polyphenols: {result['predicted_mgkg']} mg/kg (±{result['uncertainty']})")
    print(f"Estimated loss: {result['percent_loss']}%")
    print(f"Baseline exponential (no light/O2): {round(predictor.baseline_exponential(args.initial, args.days, args.temp), 1)} mg/kg")
