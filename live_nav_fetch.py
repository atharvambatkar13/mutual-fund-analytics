import requests
import pandas as pd

schemes = {
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_largecap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}

for scheme_code, scheme_name in schemes.items():

    print(f"\nFetching {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        output_file = f"data/raw/{scheme_name}_nav.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")
        print(f"Records: {len(df)}")

    else:
        print(f"Failed for {scheme_code}")