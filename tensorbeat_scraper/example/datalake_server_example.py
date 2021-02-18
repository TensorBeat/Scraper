import asyncio

from grpclib.client import Channel
from tensorbeat_scraper.generated.tensorbeat.datalake import DatalakeServiceStub


async def main():

    channel = Channel(host="grpc.test.tensorbeat.com", port=50051)
    service = DatalakeServiceStub(channel)

    res = await service.get_all_songs()

    print(res.songs)

    channel.close()


if __name__ == "__main__":
    asyncio.run(main())