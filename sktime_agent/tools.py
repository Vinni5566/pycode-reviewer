from langchain_core.tools import tool
from typing import List, Optional, Dict
import pandas as pd
from sktime.forecasting.arima import ARIMA
from sktime.forecasting.compose import ForecastingPipeline
from sktime.performance_metrics.forecasting import mean_absolute_percentage_error

@tool
def forecast_series(y: List[float], fh: List[int], model_type: str = "arima") -> List[float]:
    """
    Fits a forecaster to the series y and predicts for the forecast horizon fh.
    """
    y_series = pd.Series(y)
    if model_type == "arima":
        forecaster = ARIMA(order=(1, 1, 1))
    else:
        # Fallback to ARIMA for demo purposes
        forecaster = ARIMA()
    
    forecaster.fit(y_series)
    y_pred = forecaster.predict(fh=fh)
    return y_pred.tolist()

@tool
def build_pipeline(steps: List[Dict[str, str]]) -> str:
    """
    Generates python code for an sktime ForecastingPipeline based on provided steps.
    Example steps: [{'name': 'scaler', 'type': 'Scaler'}, {'name': 'forecaster', 'type': 'ARIMA'}]
    """
    # This tool simulates pipeline building by returning the code structure
    code = "from sktime.forecasting.compose import ForecastingPipeline\n"
    code += "pipeline = ForecastingPipeline([\n"
    for step in steps:
        code += f"    ('{step['name']}', {step['type']}()),\n"
    code += "])"
    return code

@tool
def evaluate_forecast(y_true: List[float], y_pred: List[float]) -> float:
    """
    Calculates the Mean Absolute Percentage Error (MAPE) between true and predicted values.
    """
    return float(mean_absolute_percentage_error(pd.Series(y_true), pd.Series(y_pred)))

SKTIME_TOOLS = [forecast_series, build_pipeline, evaluate_forecast]
