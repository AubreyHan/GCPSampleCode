from google.cloud import storage

def list_buckets(projectName):
    """Lists all buckets."""

    storage_client = storage.Client(project=projectName)
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

list_buckets('457346115316')