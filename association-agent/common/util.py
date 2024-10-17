import argparse

def parse_main_args():
  parser = argparse.ArgumentParser()

  parser.add_argument("--analysis_id", type=str, help="analysis id")

  parser.add_argument("--mode", type=str, help="analysis mode")
  parser.add_argument("--algorithm", type=str, help="algorithm name")

  parser.add_argument("--input_data_path", type=str, help="input_data_path")
  parser.add_argument("--output_data_path", type=str, help="output_data_path")

  parser.add_argument("--model_option", type=str, help="model hyperparameters")
  parser.add_argument("--fe_option", type=str, help="feature hyperparameters")
  parser.add_argument("--learning_option", type=str, help="learning hyperparameters")

args = parser.parse_known_args()[0]

  return vars(args)