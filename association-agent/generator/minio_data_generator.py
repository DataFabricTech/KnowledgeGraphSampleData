from minio import Minio

class MinioDataGenerator:
  def __init__(self):
    None

  def fetchMinioDataWithFilePath(self, host, port, access_key, secret_key, region, bucket_name, input_file_path, output_file_path):
    client = Minio("%s:%d"%(host, port), access_key = access_key, secret_key = secret_key, region = region, secure = False)

    try:
      client.fget_object(bucket_name, input_file_path, output_file_path)
    except ResponseError as err:
      raise err