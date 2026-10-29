# monitor.py
# monitor.py / Configure a basic Evidently data drift or model monitoring report
# monitor.py
import pandas as pd

# Compatibility patch for Python 3.13 & Pandas 2.2+/3.x
if not hasattr(pd.core.dtypes.common, 'infer_dtype_from_object'):
    try:
        from pandas.api.types import infer_dtype
        pd.core.dtypes.common.infer_dtype_from_object = infer_dtype
    except ImportError:
        pass

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Sample reference and current datasets
reference_data = pd.DataFrame({'feature_1': [1, 2, 3, 4, 5], 'target': [0, 1, 0, 1, 0]})
current_data = pd.DataFrame({'feature_1': [1, 2, 3, 4, 8], 'target': [0, 1, 0, 1, 1]})

# Generate Evidently Report
data_drift_report = Report(metrics=[DataDriftPreset()])
data_drift_report.run(reference_data=reference_data, current_data=current_data)

# Save report to HTML
data_drift_report.save("evidently_report.html")
print("Evidently monitoring report generated successfully.")