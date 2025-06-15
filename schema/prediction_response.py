from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
  predicted_category: str = Field(
      ..., description="Predicted insurance premium category",
      examples=["high"]
  )

  confidence: float = Field(
      ..., description="Confidence level of the prediction",
      examples=[0.85]
  )

  class_probabilities: Dict[str, float] = Field(
      ..., description="Probability distribution across all classes",
      examples=[{"low": 0.1, "medium": 0.3, "high": 0.6}]
  )