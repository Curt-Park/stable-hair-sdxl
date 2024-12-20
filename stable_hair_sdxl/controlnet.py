import copy

from diffusers import ControlNetModel


class StableHairControlNetModel(ControlNetModel):
    def __init__(
        self,
        in_channels: int = 4,
        conditioning_channels: int = 4,
        **kwargs,
    ) -> None:
        super().__init__(
            in_channels=in_channels,
            conditioning_channels=conditioning_channels,
            **kwargs,
        )
        self.controlnet_cond_embedding = copy.deepcopy(self.conv_in)
