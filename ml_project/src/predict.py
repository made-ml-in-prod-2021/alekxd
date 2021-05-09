import sys

import utils
from train import load_model, save_prediction, load_data, save_data, convert_df_to_numpy  

if __name__ == "__main__":
    params = utils.read_params(sys.argv[1])
    utils._init_logging(params)

    df = load_data(params.input_test_data_path)
    data = convert_df_to_numpy(df, params)
    save_data(data, params.output_test_data_path)

    X, _ = data
    model = load_model(params.output_model_path)
    prediction = model.predict(X)
    save_prediction(prediction, params.input_test_data_path, params.output_prediction_path) 
