import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
temp_data = pd.read_csv('HistoricalTempHeatIndex.csv')
hosp_data = pd.read_excel('Hospitalizations.xlsx')
mort_data = pd.read_csv('Mortality_Oct24.csv')
worker_data = pd.read_excel('WorkerHealth.xlsx')
pop_data = pd.read_excel('StatePopulations.xlsx')

# Merge datasets
merged_data = pd.merge(hosp_data, mort_data, on=['State', 'Year'], how='outer')
merged_data = pd.merge(merged_data, worker_data, on=['State', 'Year'], how='outer')
merged_data = pd.merge(merged_data, pop_data, on=['State'], how='left')

# Normalize data (per 100,000 population)
merged_data['hosp_rate'] = merged_data['Value_x'] / merged_data['Population'] * 100000
merged_data['mort_rate'] = pd.to_numeric(merged_data['Mortalities'], errors='coerce') / merged_data['Population'] * 100000
merged_data['worker_death_rate'] = pd.to_numeric(merged_data['Value_y'], errors='coerce') / merged_data['Population'] * 100000

# Ensure 'Year_x' is numeric and convert to integer
merged_data['Year_x'] = pd.to_numeric(merged_data['Year_x'], errors='coerce').astype('Int64')

# Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=merged_data, x='Year_x', y='hosp_rate', errorbar=None, label='Hospitalizations', marker='o')
sns.lineplot(data=merged_data, x='Year_x', y='mort_rate', errorbar=None, label='Mortalities', marker='s')
sns.lineplot(data=merged_data, x='Year_x', y='worker_death_rate', errorbar=None, label='Worker Deaths', marker='^')

plt.title('Heat-Related Health Incidents Over Time')
plt.xlabel('Year')
plt.ylabel('Rate per 100,000 population')

# Set x-axis to show only whole years
plt.xticks(merged_data['Year_x'].unique())

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend()

# Adjust layout to prevent cutting off labels
plt.tight_layout()

plt.show()

state_summary = merged_data.groupby('State')[['hosp_rate', 'mort_rate', 'worker_death_rate']].mean().sort_values('hosp_rate', ascending=False)
print(state_summary.head(10))  # Top 10 states by hospitalization rate

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Convert relevant columns to numeric, replacing non-numeric values with NaN
merged_data['Value_y'] = pd.to_numeric(merged_data['Value_y'], errors='coerce')
merged_data['Value_x'] = pd.to_numeric(merged_data['Value_x'], errors='coerce')
merged_data['Mortalities'] = pd.to_numeric(merged_data['Mortalities'], errors='coerce')
merged_data['Year_x'] = pd.to_numeric(merged_data['Year_x'], errors='coerce')

# Aggregate data if needed
merged_data = merged_data.groupby(['State', 'Year_x']).agg({
    'Value_y': 'mean',
    'Value_x': 'mean',
    'Mortalities': 'mean',
    'worker_death_rate': 'mean',
    'hosp_rate': 'mean',
    'mort_rate': 'mean'
}).reset_index()

# Calculate averages
avg_worker_deaths = merged_data['Value_y'].mean()
avg_hospitalizations = merged_data['Value_x'].mean()
avg_mortality = merged_data['Mortalities'].mean()

def create_chart(state_name, metric_col, avg_value, title):
    state_data = merged_data[merged_data['State'] == state_name]
    
    # Ensure we have matching year and value pairs
    valid_data = state_data[['Year_x', metric_col]].dropna()
    years = valid_data['Year_x']
    values = valid_data[metric_col]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o', label=state_name)
    plt.axhline(y=avg_value, color='r', linestyle='--', label='National Average')
    plt.title(f'{title} in {state_name} vs National Average')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create charts for each state and metric
states = ['Tennessee', 'Louisiana', 'Texas', 'California']
metrics = [
    ('Value_y', avg_worker_deaths, 'Worker Deaths'),
    ('Value_x', avg_hospitalizations, 'Hospitalizations'),
    ('Mortalities', avg_mortality, 'Mortality')
]

for state in states:
    for metric_col, avg_value, title in metrics:
        create_chart(state, metric_col, avg_value, title)

# Per capita rates
avg_worker_death_rate = merged_data['worker_death_rate'].mean()
avg_hosp_rate = merged_data['hosp_rate'].mean()
avg_mort_rate = merged_data['mort_rate'].mean()

def create_rate_chart(state_name, rate_col, avg_rate, title):
    state_data = merged_data[merged_data['State'] == state_name]
    
    # Ensure we have matching year and rate pairs
    valid_data = state_data[['Year_x', rate_col]].dropna()
    years = valid_data['Year_x']
    rates = valid_data[rate_col]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, rates, marker='o', label=state_name)
    plt.axhline(y=avg_rate, color='r', linestyle='--', label='National Average')
    plt.title(f'{title} Rate in {state_name} vs National Average')
    plt.xlabel('Year')
    plt.ylabel('Rate per 100,000 population')
    plt.legend()
    plt.grid(True)
    plt.show()

# Create charts for each state and rate metric
rate_metrics = [
    ('worker_death_rate', avg_worker_death_rate, 'Worker Death'),
    ('hosp_rate', avg_hosp_rate, 'Hospitalization'),
    ('mort_rate', avg_mort_rate, 'Mortality')
]

for state in states:
    for rate_col, avg_rate, title in rate_metrics:
        create_rate_chart(state, rate_col, avg_rate, title)

# Calculate averages
avg_worker_deaths = merged_data['Value_y'].mean()
avg_hospitalizations = merged_data['Value_x'].mean()
avg_mortality = merged_data['Mortalities'].mean()
avg_worker_death_rate = merged_data['worker_death_rate'].mean()
avg_hosp_rate = merged_data['hosp_rate'].mean()
avg_mort_rate = merged_data['mort_rate'].mean()

# States to include with their colors
states_colors = {
    'Tennessee': 'orange',
    'Texas': 'red',
    'California': 'green',
    'Louisiana': 'yellow',
    'Georgia': 'blue'
}

def create_comparison_charts(metric_col, rate_col, avg_count, avg_rate, title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
    
    for state, color in states_colors.items():
        state_data = merged_data[merged_data['State'] == state]
        ax1.plot(state_data['Year_x'], state_data[metric_col], marker='o', label=state, color=color)
        ax2.plot(state_data['Year_x'], state_data[rate_col], marker='o', label=state, color=color)
    
    ax1.axhline(y=avg_count, color='grey', linestyle='--', label='National Average')
    ax2.axhline(y=avg_rate, color='grey', linestyle='--', label='National Average')
    
    ax1.set_title(f'{title} by Count')
    ax2.set_title(f'{title} per Capita')
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Year')
    ax1.set_ylabel('Count')
    ax2.set_ylabel('Rate per 100,000 population')
    
    # Set x-axis to show only whole years
    for ax in [ax1, ax2]:
        ax.set_xticks(merged_data['Year_x'].unique())
        ax.set_xticklabels(merged_data['Year_x'].unique().astype(int))
    
    ax1.legend()
    ax2.legend()
    ax1.grid(True)
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

# 1) Worker Deaths
create_comparison_charts('Value_y', 'worker_death_rate', avg_worker_deaths, avg_worker_death_rate, 'Worker Deaths')

# 2) Hospitalizations
create_comparison_charts('Value_x', 'hosp_rate', avg_hospitalizations, avg_hosp_rate, 'Hospitalizations')

# 3) Mortality
create_comparison_charts('Mortalities', 'mort_rate', avg_mortality, avg_mort_rate, 'Mortality')

# Print average values
print(f"Average Worker Deaths: {avg_worker_deaths:.2f}")
print(f"Average Hospitalizations: {avg_hospitalizations:.2f}")
print(f"Average Mortality: {avg_mortality:.2f}")
print(f"Average Worker Death Rate: {avg_worker_death_rate:.2f} per 100,000")
print(f"Average Hospitalization Rate: {avg_hosp_rate:.2f} per 100,000")
print(f"Average Mortality Rate: {avg_mort_rate:.2f} per 100,000")

from scipy import stats

def perform_t_test(state_data, national_avg, metric):
    state_values = state_data[metric].dropna()
    if len(state_values) > 1:  # Ensure we have enough data points
        t_stat, p_value = stats.ttest_1samp(state_values, national_avg)
        return p_value
    else:
        return np.nan

states = ['Tennessee', 'Texas', 'California', 'Georgia', 'Louisiana']
metrics = [
    ('worker_death_rate', 'Worker Death Rate'),
    ('hosp_rate', 'Hospitalization Rate'),
    ('mort_rate', 'Mortality Rate')
]

results = []

for state in states:
    state_data = merged_data[merged_data['State'] == state]
    
    for metric, metric_name in metrics:
        national_avg = merged_data[metric].mean()
        p_value = perform_t_test(state_data, national_avg, metric)
        
        results.append({
            'State': state,
            'Metric': metric_name,
            'P-value': p_value,
            'Significant': 'Yes' if p_value < 0.05 else 'No' if not np.isnan(p_value) else 'Insufficient Data'
        })

results_df = pd.DataFrame(results)

# Display the results
print(results_df.to_string(index=False))

# Optionally, save to CSV
results_df.to_csv('statistical_significance_results.csv', index=False)