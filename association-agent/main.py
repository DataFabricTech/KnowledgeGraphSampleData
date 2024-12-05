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

  input_data_path = analysis_root_path + "analysis_input.csv"    
  output_data_path = analysis_root_path + "analysis_result.csv"

  if mode == "mock":

    generator = ConvergenceDataGenerator()
    generator.generateDataFrameWithFilePath(input_data_path)
  else:
    if datasource_type == "MinIO":
      host = args["host"]
      port = args["port"]
      region = args["region"]
      bucket_name = args["bucket_name"]
      access_key = args["access_key"]
      secret_key = args["secret_key"]
      data_source_path = args["file_source_path"]
      loaded_data_path = input_data_path

      generator = MinioDataGenerator()
      generator.fetchMinioDataWithFilePath(host, port, access_key, secret_key, region, bucket_name, data_source_path, loaded_data_path)

  if algorithm == "association-analysis":
    runner = AssociationRuleCFRunner(input_data_path, output_data_path)
    runner.run()