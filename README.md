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

- **Best Model**: Random Forest (F1-score: 0.86).
- **Top Features**: `Oldpeak`, `MaxHR`,`Age` and `ST_Slope`.
- **ROC-AUC**: 0.94.

### Visualizations

![ROC Curve](outputs/roc_curve.png)
![Feature Importance](outputs/feature_importance.png)
![Shap_summary](outputs/shap_summary.png)

## **Day 3: Model Deployment**

### API Endpoint

`POST /predict`
**Input**:

```json
{
  "Age": 58,
  "Sex": 1,
  "ChestPainType_ATA": 1,
  "RestingBP": 140,
  "Cholesterol": 289,
  "MaxHR": 172,
  "Oldpeak": 0.0
}

**OUTPUT**:
{"prediction": 1}
