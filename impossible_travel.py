import pandas as pd

df = pd.read_csv("sample_logs.csv")

print("=== Login Records ===")
print(df)

print("\n=== Impossible Travel Alerts ===")

for user in df["User"].unique():

    user_data = df[df["User"] == user]

    if len(user_data) >= 2:

        first = user_data.iloc[0]
        second = user_data.iloc[1]

        if first["Location"] != second["Location"]:

            print("\nALERT: Impossible Travel Detected")
            print("User:", user)
            print("Login 1:", first["Location"], "-", first["Login_Time"])
            print("Login 2:", second["Location"], "-", second["Login_Time"])