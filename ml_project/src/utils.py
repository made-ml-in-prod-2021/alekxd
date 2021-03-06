from dataclasses import dataclass, field
from typing import List, Optional
from marshmallow_dataclass import class_schema
import yaml
import sys
import logging

@dataclass()
class Params:
    input_train_data_path: str
    input_test_data_path: str
    output_train_data_path: str
    output_test_data_path: str
    output_model_path: str
    output_prediction_path: str
    log_file_path: Optional[str]

    @dataclass()
    class PrepareParams:
        categorical_features: List[str]
        numerical_features: List[str]
        target_col: Optional[str]    
    prepare_params: PrepareParams

    @dataclass()
    class TrainParams:
        model_type: str
        model_params: str
        val_size: float = field(default=0.2)
        random_state: int = field(default=255)
    train_params: TrainParams

ParamsSchema = class_schema(Params)

def read_params(path):
    with open(path, "r") as input_stream:
        schema = ParamsSchema()
        return schema.load(yaml.safe_load(input_stream))

def _init_logging(params):
    handlers = [logging.StreamHandler(sys.stdout)]
    if params.log_file_path:
        handlers += [logging.FileHandler(params.log_file_path)]

    logging.basicConfig(
        level=logging.INFO,     
        handlers=handlers
    )

if __name__ == "__main__":
    print(read_params(sys.argv[1]))
