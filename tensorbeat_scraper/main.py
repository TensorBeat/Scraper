from dotenv import load_dotenv

load_dotenv()
import os

print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))


import asyncio

from grpclib.client import Channel

from tensorbeat_scraper.generated.protos.common import File
from tensorbeat_scraper.generated.protos.datalake import DatalakeServiceStub


from google.cloud import storage


async def main():
    # channel = Channel(host="127.0.0.1", port=50051)

    # data_service = DatalakeServiceStub(channel)

    # song = File("gs://", {"genre": "rock"})
    # response = await data_service.add_songs(songs=[song])
    # print(response)

    storage_client = storage.Client()

    bucket = storage_client.bucket("test-tensorbeat-songs")

    blob = bucket.blob("song.mp3")
    blob.download_to_filename("song.mp3")

    # # don't forget to close the channel when done!
    # channel.close()


# Entrypoint for poetry run main
def init():
    asyncio.run(main())


if __name__ == "__main__":
    init()