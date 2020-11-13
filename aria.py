import aria2p
import socket
import os
host = socket.gethostbyname(socket.gethostname())

aria2 = aria2p.API(
    aria2p.Client(
        host=f"http://{host}",
        secret=os.environ.get("RPC_SECRET")
    )
)

# initialization, these are the default values
aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)

# list downloads
downloads = aria2.get_downloads()

for download in downloads:
    print(download.name, download.download_speed)

# add downloads
magnet_uri = "magnet:?xt=urn:..."

download = aria2.add_magnet(magnet_uri)
