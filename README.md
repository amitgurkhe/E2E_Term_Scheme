# E2E_Term_Scheme
To predict whether a person would by the scheme or not

1. Check artifacts/model_evaluation/metrics.json for model performance.
2. Recall of 0.428 is at the threshold of 0.5.
3. It can be improved to 0.66 if the threshold is fixed at 0.270, which is needed to overcome the imbalance in the target variable.
4. After threshold tuning it also gives a precision of 0.57 and f1_score of 0.61
5. More emphasise have been given on recall as our problem statement states that there should be very less loss of business (i.e False Negatives).
6. With this recall the campaign will be profitable as there are good number of True Positives.
