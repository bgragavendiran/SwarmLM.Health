from petals.constants import PUBLIC_INITIAL_PEERS

from data_structures import ModelInfo

INITIAL_PEERS = [
   "/ip4/130.250.185.236/tcp/32722/p2p/QmSzvetBZaMdeprswgBCLwEZtk2WjGGeXwmChmfWKPmQCK"
]

MODELS = [
    ModelInfo(
        dht_prefix="StableBeluga2-7B",
        repository="https://huggingface.co/petals-team/StableBeluga2",
        num_blocks=80,
    )
]

UPDATE_PERIOD = 60
