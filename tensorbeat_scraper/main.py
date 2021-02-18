from tensorbeat_scraper.generated.tensorbeat.common import AddFile
from dotenv import load_dotenv

load_dotenv()
import os

print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))


import asyncio

from grpclib.client import Channel

from grpclib.client import Channel
from tensorbeat_scraper.generated.tensorbeat.datalake import DatalakeServiceStub

from google.cloud import storage


async def main():

    channel = Channel(host="grpc.test.tensorbeat.com", port=50051)
    datalake = DatalakeServiceStub(channel)

    res = await datalake.get_all_songs()

    print(res.songs)

    # This downloads a file from a cloud bucket
    # This link shows how to upload:
    # https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python

    storage_client = storage.Client()

    bucket = storage_client.bucket("test-tensorbeat-songs")

    blob = bucket.blob("song.mp3")
    blob.download_to_filename("song.mp3")

    # upload the file

    file = AddFile(
        mime_type="audio/mpeg",
        name="Test",
        tags={"genre": "rock"},
        uri="gs://test-tensorbeat-songs/song.mp3",
    )

    # to actually add to datalake
    # datalake.add_songs([file])

    # # don't forget to close the channel when done!
    # channel.close()


# Entrypoint for poetry run main
def init():
    asyncio.run(main())


if __name__ == "__main__":
    init()