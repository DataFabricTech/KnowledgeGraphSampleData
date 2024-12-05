from minio import Minio

class MinioDataGenerator:
  def __init__(self):
    None

  def fetchMinioDataWithFilePath(self, host, port, access_key, secret_key, region, bucket_name, file_source_path, loaded_data_path):
    print("%s:%s"%(host, port))
    client = Minio("%s:%s"%(host, port), access_key = access_key, secret_key = secret_key, region = region, secure = False)

    print(bucket_name, file_source_path)
    try:
      client.fget_object(bucket_name, file_source_path, loaded_data_path)
    except ResponseError as err:
      raise err