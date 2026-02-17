import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Title
ax.text(5, 11.5, 'Alternative Credit Scoring System Architecture', 
        ha='center', fontsize=20, fontweight='bold')

# ============ DATA SOURCES LAYER ============
ax.text(5, 10.5, 'DATA SOURCES', ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black', linewidth=2))

# Data source boxes
data_sources = [
    ('Application\\nData', 1, 9.5),
    ('Bureau\\nHistory', 2.5, 9.5),
    ('Previous\\nLoans', 4, 9.5),
    ('POS/Cash\\nBalance', 5.5, 9.5),
    ('Installments\\nPayments', 7, 9.5),
    ('CFPB\\nComplaints', 8.5, 9.5)
]

for label, x, y in data_sources:
    box = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, boxstyle='round,pad=0.05',
                         facecolor='#e8f4f8', edgecolor='#2980b9', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# ============ PREPROCESSING LAYER ============
arrow1 = FancyArrowPatch((5, 9.2), (5, 8.5), arrowstyle='->', mutation_scale=30, 
                         linewidth=3, color='black')
ax.add_patch(arrow1)

ax.text(5, 8.2, 'PREPROCESSING & FEATURE ENGINEERING', ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgreen', edgecolor='black', linewidth=2))

preprocessing_steps = [
    ('Missing Value\\nImputation', 1.5, 7.2),
    ('Outlier\\nTreatment', 3.5, 7.2),
    ('Feature\\nAggregation', 5.5, 7.2),
    ('Feature\\nScaling', 7.5, 7.2)
]

for label, x, y in preprocessing_steps:
    box = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, boxstyle='round,pad=0.05',
                         facecolor='#d5f4e6', edgecolor='#27ae60', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# ============ FEATURE TYPES LAYER ============
arrow2 = FancyArrowPatch((5, 6.9), (5, 6.2), arrowstyle='->', mutation_scale=30,
                         linewidth=3, color='black')
ax.add_patch(arrow2)

ax.text(5, 5.9, 'FEATURE CATEGORIES', ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='black', linewidth=2))

feature_types = [
    ('Traditional\\nFeatures\\n(Income, Age)', 2, 5),
    ('Alternative\\nData Features\\n(Bureau, POS)', 5, 5),
    ('Social\\nFeatures\\n(Geographic)', 8, 5)
]

for label, x, y in feature_types:
    box = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8, boxstyle='round,pad=0.05',
                         facecolor='#fff9e6', edgecolor='#f39c12', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# ============ MODEL LAYER ============
arrow3 = FancyArrowPatch((5, 4.6), (5, 3.9), arrowstyle='->', mutation_scale=30,
                         linewidth=3, color='black')
ax.add_patch(arrow3)

ax.text(5, 3.6, 'MACHINE LEARNING MODELS', ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffcccc', edgecolor='black', linewidth=2))

models = [
    ('Logistic\\nRegression\\n(Baseline)', 1.5, 2.7),
    ('Random\\nForest', 3.5, 2.7),
    ('XGBoost', 5.5, 2.7),
    ('LightGBM', 7.5, 2.7)
]

for label, x, y in models:
    box = FancyBboxPatch((x-0.4, y-0.3), 0.8, 0.6, boxstyle='round,pad=0.05',
                         facecolor='#ffe6e6', edgecolor='#c0392b', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# ============ EVALUATION LAYER ============
arrow4 = FancyArrowPatch((5, 2.4), (5, 1.7), arrowstyle='->', mutation_scale=30,
                         linewidth=3, color='black')
ax.add_patch(arrow4)

ax.text(5, 1.4, 'MODEL EVALUATION & INTERPRETATION', ha='center', fontsize=14, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#e6ccff', edgecolor='black', linewidth=2))

eval_metrics = [
    ('ROC-AUC\\nScore', 2, 0.6),
    ('Precision-\\nRecall', 4, 0.6),
    ('SHAP\\nValues', 6, 0.6),
    ('Confusion\\nMatrix', 8, 0.6)
]

for label, x, y in eval_metrics:
    box = FancyBboxPatch((x-0.4, y-0.25), 0.8, 0.5, boxstyle='round,pad=0.05',
                         facecolor='#f3e6ff', edgecolor='#8e44ad', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold')

# Add legend
legend_elements = [
    mpatches.Patch(facecolor='#e8f4f8', edgecolor='#2980b9', label='Data Sources'),
    mpatches.Patch(facecolor='#d5f4e6', edgecolor='#27ae60', label='Preprocessing'),
    mpatches.Patch(facecolor='#fff9e6', edgecolor='#f39c12', label='Features'),
    mpatches.Patch(facecolor='#ffe6e6', edgecolor='#c0392b', label='Models'),
    mpatches.Patch(facecolor='#f3e6ff', edgecolor='#8e44ad', label='Evaluation')
]

ax.legend(handles=legend_elements, loc='lower right', fontsize=10, frameon=True,
          fancybox=True, shadow=True)

plt.tight_layout()
plt.savefig('visualizations/06_system_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Architecture diagram created successfully in visualizations/06_system_architecture.png")
