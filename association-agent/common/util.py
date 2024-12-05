import argparse

def parse_main_args():
  parser = argparse.ArgumentParser()

  parser.add_argument("--analysis_id", type=str, help="analysis id")

  parser.add_argument("--mode", type=str, help="analysis mode")
  parser.add_argument("--algorithm", type=str, help="algorithm name")

  parser.add_argument("--file_source_path", type=str, help="input file source path")

  parser.add_argument("--model_option", type=str, help="model hyperparameters")
  parser.add_argument("--fe_option", type=str, help="feature hyperparameters")
  parser.add_argument("--learning_option", type=str, help="learning hyperparameters")

  parser.add_argument("--datasource_type", type=str, help="datasource vendor")
  
  parser.add_argument("--host", type=str, help="MinIO datasource host")
  parser.add_argument("--port", type=str, help="MinIO datasource port")
  parser.add_argument("--region", type=str, help="MinIO datasource region")
  parser.add_argument("--bucket_name", type=str, help="Minio datasource bucket name")
  parser.add_argument("--access_key", type=str, help="MinIO datasource Access Key")
  parser.add_argument("--secret_key", type=str, help="MinIO datasource Secret Key")

  args = parser.parse_known_args()[0]

  return vars(args)