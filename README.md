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
![Incidents_TimeSeries](Images\Incidents_TimeSeries.png)

##### Hospitalization rates
1. Arizona stands out with the highest hospitalization rate at **1.074 per 100,000**.
2. Louisiana
3. South Carolina
4. Kansas
5. Tennessee

##### Mortality rates 
Arizona also has the highest heat-related mortality rate at **4.128 per 100,000**. That's significantly higher than its hospitalization rate, interestingly.

Maryland has the second-highest mortality rate, though it has a relatively low hospitalization rate.
     
##### Worker death rates
Tennessee has the highest worker death rate at **2.875 per 100,000** (despite being fifth in hospitalizations).
2. Arizona
3. Maryland
4. Virginia

### States of interest
Here's how our target states compare to the national average and to each other.

#### Hospitalization rates
![Hospitalizations](Images\Hospitaliizations_Comparisons.png)
![Hospitalizations_Cali](Images\Cali_vs_Natl_HospRate.png)
![Hospitalizations_LA](Images\La_vs_Natl_HospRate.png)
![Hospitalizations_Tenn](Images\Tenn_vs_Natl_HospRate.png)
**Note: Neither Georgia nor Texas reported hospitalization rates.**

#### Mortality rates
![Mortality](Images\Deaths_Comparisons.png)
![Mortality_Cali](Images\Cali_vs_Natl_MortRate.png)
![Mortality_LA](Images\La_vs_Natl_MortRate.png)
![Mortality_Tenn](Images\Tenn_vs_Natl_MortRate.png)
![Mortality_Texas](Images\Texas_vs_Natl_MortRate.png)

#### Worker death rates
![WorkerDeaths](Images\WorkerDeaths_Comparisons.png)
![Worker_Cali](Images\Cali_vs_Natl_WorkerRate.png)
![Worker_LA](Images\La_vs_Natl_WorkerRate.png)
![Worker_Tenn](Images\Tenn_vs_Natl_WorkerRate.png)
![Worker_Texas](Images\Texas_vs_Natl_WorkersRate.png)

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
