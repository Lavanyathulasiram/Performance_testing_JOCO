import pandas as pd

def update_excel(filepath, results):
    df = pd.DataFrame(results)
    df.to_excel(filepath, index=False)
    print(f"Excel updated with {len(results)} rows at:\n{filepath}")
