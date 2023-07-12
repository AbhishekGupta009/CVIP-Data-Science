# -*- coding: utf-8 -*-
"""Golden_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sCWGVopFD_JeeiUboNyCoR8jyXi9pLXU
"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
data = pd.read_csv('/content/Breast Cancer Dataset.csv')

# Data preprocessing
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Map 'B' to 0 and 'M' to 1
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Feature selection using SelectKBest and ANOVA F-value
selector = SelectKBest(f_classif, k=20)
X_new = selector.fit_transform(X, y)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_new)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Create an SVM classifier
classifier = SVC(kernel='linear')

# Cross-validation
cv_scores = cross_val_score(classifier, X_scaled, y, cv=5)
print('Cross-validation scores:', cv_scores)
print('Mean cross-validation score:', cv_scores.mean())

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


# Plot precision-recall curve
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_test, y_scores)

plt.figure(figsize=(8, 6))
plt.plot(recall, precision, label='Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='lower left')
plt.show()

# Generate evaluation metrics
classification_rep = classification_report(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
print('Classification Report:\n', classification_rep)
print('Confusion Matrix:\n', confusion_mat)

# Visualize feature importance
feature_names = data.drop('diagnosis', axis=1).columns
feature_scores = selector.scores_
feature_importance = pd.DataFrame({'Feature': feature_names, 'Score': feature_scores})
feature_importance = feature_importance.nlargest(10, 'Score')

plt.figure(figsize=(12, 6))
sns.barplot(x='Score', y='Feature', data=feature_importance)
plt.title('Feature Importance')
plt.xlabel('Score')
plt.ylabel('Feature')
plt.show()

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()

# Plot ROC curve
from sklearn.metrics import roc_curve, auc

y_scores = classifier.decision_function(X_test)
fpr, tpr, _ = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='ROC Curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0, 1])
plt.ylim([0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()
