import pandas as pd
import sys

def combine_temp(trips_file, temp_file, output_file):
    trips_df = pd.read_csv(trips_file)
    temp_df = pd.read_csv(temp_file)

    combined_df = pd.merge(trips_df, temp_df, on='date', how='left')
    combined_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    combine_temp(sys.argv[1], sys.argv[2], sys.argv[3])