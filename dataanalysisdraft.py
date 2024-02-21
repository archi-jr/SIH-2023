import pandas as pd

# Load your dataset
data = pd.read_csv('patients_data.csv')

# Find the top 3 spreading diseases
top_spreading_diseases = data['Disease'].value_counts().head(3).index

# Find the top 3 consumed medicines
top_consumed_medicines = data['Medicine'].value_counts().head(3).index

print("Top 3 Spreading Diseases:")
for disease in top_spreading_diseases:
    print(f"Disease: {disease}")
    filtered_data = data[data['Disease'] == disease]

    # Define the updated age groups
    age_groups = ['0-2', '3-5', '6-13', '14-18', '19-35', '36-65', '65-80', '80+']

    # Predict the age range most at risk
    filtered_data['AgeGroup'] = pd.cut(filtered_data['Age'], bins=[0, 2, 5, 13, 18, 35, 65, 80, 150], labels=age_groups)

    age_group_counts = filtered_data['AgeGroup'].value_counts()

    for age_group, count in age_group_counts.items():
        print(f"Age Group: {age_group}, Count: {count}")
    print()

print("\nTop 3 Consumed Medicines:")
for medicine in top_consumed_medicines:
    print(f"Medicine: {medicine}")
    filtered_data = data[data['Medicine'] == medicine]

    # Define the updated age groups
    age_groups = ['0-2', '3-5', '6-13', '14-18', '19-35', '36-65', '65-80', '80+']

    # Predict the age range most at risk
    filtered_data['AgeGroup'] = pd.cut(filtered_data['Age'], bins=[0, 2, 5, 13, 18, 35, 65, 80, 150], labels=age_groups)

    age_group_counts = filtered_data['AgeGroup'].value_counts()

    for age_group, count in age_group_counts.items():
        print(f"Age Group: {age_group}, Count: {count}")
    print()
# Find the top 3 spreading diseases
top_spreading_diseases = data['Disease'].value_counts().head(3).index

# Find the top 3 consumed medicines
top_consumed_medicines = data['Medicine'].value_counts().head(3).index

# Create a new DataFrame to store the results
result_df = pd.DataFrame(columns=['Disease', 'Affected People', 'Medicine Required'])
result1_df = pd.DataFrame(columns=['Disease', 'Affected People', 'Medicine Required'])

for disease in top_spreading_diseases:
    filtered_data = data[data['Disease'] == disease]

    # Calculate the number of people affected by the disease
    affected_people = len(filtered_data)

    # Find the medicine required for the disease
    medicine_required = filtered_data['Medicine'].iloc[
        0]  # Assuming the same medicine for all rows with the same disease

    # Append the results to the result DataFrame
    result_df = result_df._append(
        {'Disease': disease, 'Affected People': affected_people, 'Medicine Required': medicine_required},
        ignore_index=True)
print("top_spreading_diseases\n")
print(result_df, "\n")

for medicine in top_consumed_medicines:
    filtered_data = data[data['Medicine'] == medicine]

    # Calculate the number of people requiring the medicine
    required_people = len(filtered_data)

    # Append the results to the result DataFrame
    result1_df = result1_df._append({'': '', 'Affected People': required_people, 'Medicine Required': medicine},
                                   ignore_index=True)
print("top_consumed_medicines\n")
print(result1_df, "\n")

result_df = result_df._append(result1_df)

# Save the result DataFrame to a CSV file
result_df.to_csv('top_diseases_and_medicines.csv', index=False)

print("Data saved to 'top_diseases_and_medicines.csv'")
# print(result_df)