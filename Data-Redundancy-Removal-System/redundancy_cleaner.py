import pandas as pd

def remove_duplicates(input_file, output_file):

    df = pd.read_csv(input_file)

    print("Original Records:", len(df))

    df = df.drop_duplicates()

    print("After Cleaning:", len(df))

    df.to_csv(output_file, index=False)

    print("Cleaned file saved.")