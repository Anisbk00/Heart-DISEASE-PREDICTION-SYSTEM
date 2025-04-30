"# Heart-DISEASE-PREDICTION-SYSTEM" 

## **Day 1: Exploratory Data Analysis**
### Key Findings
- **Age**: Patients with heart disease tend to be older (median ~58 vs. 53).
- **Cholesterol**: Higher cholesterol levels correlate with heart disease.
- **Sex**: Males have a higher prevalence of heart disease.
- **Chest Pain**: Asymptomatic chest pain is most common in heart disease patients.

### Visualizations
![Age vs. Heart Disease](outputs/age_vs_heartdisease.png)
![Chest Pain vs. Heart Disease](outputs/chestpain_vs_heartdisease.png)
![Correlation Heatmap](outputs/correlation_heatmap.png)

## Day 2: Model Building & Evaluation  
### Key Results  
- **Best Model**: Random Forest (F1-score: 0.89).  
- **Top Features**: `Oldpeak`, `MaxHR`, and `ChestPainType_ATA`.  
- **ROC-AUC**: 0.93.  

### Visualizations  
![ROC Curve](outputs/roc_curve.png)  
![Feature Importance](outputs/feature_importance.png)  