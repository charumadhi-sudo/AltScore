import pickle
import joblib
import lightgbm as lgb
import sys

filepath = 'models/lightgbm.pkl'
print("Trying joblib...")
try:
    model = joblib.load(filepath)
    print("Success with joblib!")
    sys.exit(0)
except Exception as e:
    print("Joblib failed:", e)

print("Trying lightgbm native...")
try:
    model = lgb.Booster(model_file=filepath)
    print("Success with lightgbm native!")
    sys.exit(0)
except Exception as e:
    print("LightGBM native failed:", e)
