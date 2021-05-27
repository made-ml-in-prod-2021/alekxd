import sys

import utils
from models import load_data, convert_df_to_numpy, save_data, train, save_model

if __name__ == "__main__":
    params = utils.read_params(sys.argv[1])
    utils._init_logging(params)
    
    df = load_data(params.input_train_data_path)
    data = convert_df_to_numpy(df, params)
    save_data(data, params.output_train_data_path)
    X, y = data
    model = train(X, y, params)
    save_model(model, params.output_model_path)

