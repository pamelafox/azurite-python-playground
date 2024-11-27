import logging
import os

from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.WARNING,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger("blobscript")
logger.setLevel(logging.INFO)

blob_service_client = BlobServiceClient.from_connection_string(
    conn_str=os.getenv("AZURE_STORAGE_CONNECTION_STRING")
)

container_name = "mycontainer"
try:
    container_client = blob_service_client.create_container(name=container_name)
    logger.info("Created container %s", container_name)
except ResourceExistsError:
    logger.info("A container with the name %s already exists", container_name)

container_client = blob_service_client.get_container_client(container=container_name)
filename = "README.md"
with open(file=filename, mode="rb") as data:
    blob_client = container_client.upload_blob(name=filename, data=data, overwrite=True)
    logger.info("Uploaded file %s to container %s", filename, container_name)

logger.info("Listing blobs in container %s", container_name)
blob_list = container_client.list_blobs()
for blob in blob_list:
    logger.info("Blob name: %s", blob.name)
