import os
from common.util import parse_main_args
from generator.convergence_data_generator import ConvergenceDataGenerator
from generator.minio_data_generator import MinioDataGenerator
from runner.collaborative_filtering_association_analysis_runner import AssociationRuleCFRunner

if __name__ == "__main__":
  args = parse_main_args()
  mode = args["mode"]
  datasource_type = args["datasource_type"]
  algorithm = args["algorithm"]
  analysis_id = args["analysis_id"]

  analysis_root_path = "/pvc/mnt/analysis-%s/"%analysis_id
  os.makedirs(analysis_root_path)

  output_data_path = analysis_root_path + "association_rule_result.csv"

  if mode == "mock":
    generator = ConvergenceDataGenerator()
    generator.generateDataFrameWithFilePath(mock_input_file_path)

    mock_input_data_path = analysis_root_path + "mock_input_data.csv"    
    args["input_data_path"] = mock_input_data_path
  else:
    if datasource_type == "MinIO":
      host = args["host"]
      port = args["port"]
      region = args["region"]
      access_key = args["access_key"]
      secret_key = args["secret_key"]
      input_data_path = args["input_data_path"]

      generator = MinioDataGenerator()
      generator.fetchMinioDataWithFilePath(host, port, access_key, secret_key, region, input_data_path, output_data_path)

  if algorithm == "association-analysis":
    runner = AssociationRuleCFRunner(args)
    runner.run()