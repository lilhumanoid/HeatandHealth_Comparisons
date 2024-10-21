# CDC Heat and Health Index: Comparing target states

Drawing from [Center for Disease Control and Prevention (CDC) Heat & Health Tracker](https://ephtracking.cdc.gov/Applications/heatTracker/) data, we're analyzing how heat may affect human health in a number of states, particularly  marginalized residents. **States of interest are California, Georgia, Louisiana, Tennessee, and Texas.**

The calculations in this section reflect per-capita rates rather than counts.

### Key metrics: Average heat-related health incidents per year
These are nationwide metrics we'll compare our target states against.
| **Measure**  | Value         
| :----------- | :--------------: 
| Average worker deaths         | 88.1
| Average hospitalizations         | 20.2
| Average deaths         | 38.3
| Average worker death rate         | 1.06 per 100,000
| Average hospitalization rate         | 0.31 per 100,000
| Average mortality rate         | 0.48 per 100,000

### Major takeaways for each metric
Looking at all states, we identified these significant observations.
![Incidents_TimeSeries](https://github.com/user-attachments/assets/5384759d-962f-4cbc-a907-83d9caf38bcd)

#### Hospitalization rates
1. Arizona stands out with the highest hospitalization rate at **1.074 per 100,000**.
2. Louisiana
3. South Carolina
4. Kansas
5. Tennessee

#### Mortality rates 
Arizona also has the highest heat-related mortality rate at **4.128 per 100,000**. That's significantly higher than its hospitalization rate, interestingly.

Maryland has the second-highest mortality rate, though it has a relatively low hospitalization rate.
     
#### Worker death rates
Tennessee has the highest worker death rate at **2.875 per 100,000** (despite being fifth in hospitalizations).
2. Arizona
3. Maryland
4. Virginia

### States of interest
Here's how our target states compare to the national average and to each other.

#### Hospitalization rates
![Hospitaliizations_Comparisons](https://github.com/user-attachments/assets/3fdf2459-e694-43a8-b0ee-39b698c951f3)
![Cali_vs_Natl_HospRate](https://github.com/user-attachments/assets/80e22f62-00df-4556-b013-9b21d1a59fc1)
![La_vs_Natl_HospRate](https://github.com/user-attachments/assets/1ba4be54-2572-40f5-ad25-65d62667f529)
![Tenn_vs_Natl_HospRate](https://github.com/user-attachments/assets/80526a79-83f4-447f-a65f-95ae6337ad07)

**Note: Neither Georgia nor Texas reported hospitalization rates.**

#### Mortality rates
![Deaths_Comparisons](https://github.com/user-attachments/assets/2a014306-7847-47f1-8f5a-5b00951c33be)
![Cali_vs_Natl_MortRate](https://github.com/user-attachments/assets/aee574c8-992e-4390-b5a1-14386222fbd4)
![La_vs_Natl_MortRate](https://github.com/user-attachments/assets/3a6690ca-2616-4121-b8b4-1ba2748654f6)
![Tenn_vs_Natl_MortRate](https://github.com/user-attachments/assets/29f5dce0-b221-4d24-a142-894213019087)
![Texas_vs_Natl_MortRate](https://github.com/user-attachments/assets/d94dc588-85e5-413c-a2d7-ecb2328c8a14)

#### Worker death rates
![WorkerDeaths_Comparisons](https://github.com/user-attachments/assets/763bfbd0-4888-4beb-94a5-2bc74f791248)
![Cali_vs_Natl_WorkerRate](https://github.com/user-attachments/assets/995a73fd-55dc-49d8-8f1a-04380ac8fd20)
![La_vs_Natl_WorkerRate](https://github.com/user-attachments/assets/aa82c9d8-5674-46aa-bab3-942ab6502e48)
![Tenn_vs_Natl_WorkerRate](https://github.com/user-attachments/assets/8c6e520f-14da-4eba-b3e4-a447a5e190b9)
![Texas_vs_Natl_WorkersRate](https://github.com/user-attachments/assets/9e303fbc-5409-4495-acf1-9ed1cb0f2966)

#### Significance of rates
| State | Measure | p-value | Significant? |
|----------|----------|----------|----------|
| California | Worker Death | 0.147620 | No |
| California | Hospitalization | 0.115948 | No |
| California | Mortality | 0.019033 | Yes |
| Georgia | Worker Death | 0.067099 | No |
| Georgia | Mortality | 0.007457 | **Yes** |
| Louisiana | Worker Death | 0.747812 | No |
| Louisiana | Hospitalization |  0.044646 | **Yes** |
| Louisiana | Mortality| 0.786962  | No |
| Tennessee | Worker Death |  0.316385 | No |
| Tennessee | Hospitalization | 0.440728 | No |
| Tennessee | Mortality | 0.003646 | **Yes** |
| Texas | Worker Death | 0.498216 | No |
| Texas | Mortality | 0.000632 | **Yes** |
