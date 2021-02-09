import asyncio
from typing import Dict, List, Optional

from grpclib.client import Channel
from grpclib.server import Server

from tensorbeat_scraper.generated.protos.common import File
from tensorbeat_scraper.generated.protos.datalake import (
    AddSongsRequest,
    AddSongsResponse,
    DatalakeServiceBase,
    DatalakeServiceStub,
    GetSongsRequest,
    GetSongsResponse,
)


class DatalakeService(DatalakeServiceBase):
    async def get_songs(self, metadata: Dict[str, str]) -> GetSongsResponse:
        response = GetSongsResponse()
        return response

    async def add_songs(self, songs: Optional[List[File]]) -> AddSongsResponse:
        response = AddSongsResponse(successful=True)
        print(songs)
        return response


async def start_server():
    HOST = "127.0.0.1"
    PORT = 50051
    service = DatalakeService()
    server = Server([service])
    await server.start(HOST, PORT)


async def main():
    await start_server()
    channel = Channel(host="127.0.0.1", port=50051)

    data_service = DatalakeServiceStub(channel)

    song = File("gs://", {"genre": "rock"})
    response = await data_service.add_songs(songs=[song])
    print(response)

    # don't forget to close the channel when done!
    channel.close()


if __name__ == "__main__":
    asyncio.run(main())
