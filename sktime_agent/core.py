from pydantic import BaseModel
from typing import Optional

class AgentResponse(BaseModel):
    task_type: str
    explanation: str
    code: str
    evaluation: Optional[str] = None

def generate_response(query: str, use_agent: bool = False) -> AgentResponse:
    """
    Main entry point for generating responses.
    """
    if use_agent:
        from .agent import SktimeAgent
        agent = SktimeAgent()
        return agent.generate_workflow(query)
    
    return AgentResponse(
        task_type="forecasting",
        explanation="[MVP Dummy] I've generated a simple ARIMA forecasting pipeline using sktime.",
        code="from sktime.forecasting.arima import ARIMA\n"
             "from sktime.transformations.series.scaler import Scaler\n"
             "from sktime.forecasting.compose import ForecastingPipeline\n\n"
             "forecaster = ForecastingPipeline([\n"
             "    ('scaler', Scaler()),\n"
             "    ('forecaster', ARIMA(order=(1, 1, 1)))\n"
             "])\n"
             "forecaster.fit(y_train)\n"
             "y_pred = forecaster.predict(fh=[1, 2, 3])",
        evaluation="from sktime.performance_metrics.forecasting import mean_absolute_percentage_error\n"
                   "mape = mean_absolute_percentage_error(y_test, y_pred)"
    )

def generate_dummy_response(query: str) -> AgentResponse:
    return generate_response(query, use_agent=False)
