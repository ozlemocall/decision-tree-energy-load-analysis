import pandas as pd
from joblib import load

FEATURES = [
    "load_ratio",
    "generation_ratio",
    "battery_soc",
    "critical_load",
    "hour",
]

CLASS_NAMES = {
    0: "Normal",
    1: "Low-load shedding",
    2: "Medium-load shedding",
    3: "Critical-load shedding",
}

def main():
    model = load("models/decision_tree_model.joblib")

    print("=== Energy Load Classification ===")
    values = {
        "load_ratio": float(input("Load ratio (%): ")),
        "generation_ratio": float(input("Generation ratio (%): ")),
        "battery_soc": float(input("Battery SOC (%): ")),
        "critical_load": int(input("Critical load? (0=No, 1=Yes): ")),
        "hour": int(input("Hour (0-23): ")),
    }

    row = pd.DataFrame([values], columns=FEATURES)
    prediction = int(model.predict(row)[0])

    print("\nDecision:", CLASS_NAMES[prediction])

if __name__ == "__main__":
    main()
