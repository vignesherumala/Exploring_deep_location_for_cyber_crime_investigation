import pandas as pd

# Load the original data
df = pd.read_csv("Generate_Synthetic_Data.csv")

# New synthetic cybercrime data for 2025
new_data = [
    {
        "timestamp": "2025-01-10 08:45:00",
        "act13": 1,
        "act420": 0,
        "latitude": 28.6139,
        "longitude": 77.2090,
        "incident_type": "Phishing",
        "region": "Delhi",
        "loss_amount": 65000
    },
    {
        "timestamp": "2025-02-22 16:30:00",
        "act13": 1,
        "act420": 1,
        "latitude": 19.0760,
        "longitude": 72.8777,
        "incident_type": "Investment Fraud",
        "region": "Mumbai",
        "loss_amount": 125000
    },
    {
        "timestamp": "2025-03-11 11:20:00",
        "act13": 1,
        "act420": 1,
        "latitude": 13.0827,
        "longitude": 80.2707,
        "incident_type": "Job Fraud",
        "region": "Chennai",
        "loss_amount": 90000
    },
    {
        "timestamp": "2025-04-05 14:55:00",
        "act13": 1,
        "act420": 0,
        "latitude": 22.5726,
        "longitude": 88.3639,
        "incident_type": "Digital Arrest Scam",
        "region": "Kolkata",
        "loss_amount": 72000
    },
    {
        "timestamp": "2025-05-18 10:10:00",
        "act13": 1,
        "act420": 0,
        "latitude": 17.3850,
        "longitude": 78.4867,
        "incident_type": "Phishing",
        "region": "Hyderabad",
        "loss_amount": 58000
    }
]

# Create DataFrame for new data
new_df = pd.DataFrame(new_data)

# Append new data to original data
updated_df = pd.concat([df, new_df], ignore_index=True)

# Save the updated data
updated_df.to_csv("data_updated_2025.csv", index=False)

print("✅ Updated data saved as 'data_updated_2025.csv'")
