from src.bigdata1.api import get_results, raise_for_status
from requests import get
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

if __name__ == "__main__":
    
    ap.add_argument("--data_url", type=str)
    ap.add_argument("--file_name", type=str)
    args = ap.parse_args()

    get_results(args.data_url, args.file_name)