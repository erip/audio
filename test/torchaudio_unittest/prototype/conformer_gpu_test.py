import torch
from torchaudio_unittest.common_utils import skipIfNoCuda, PytorchTestCase
from torchaudio_unittest.prototype.conformer_test_impl import ConformerTestImpl


@skipIfNoCuda
class ConformerFloat32GPUTest(ConformerTestImpl, PytorchTestCase):
    dtype = torch.float32
    device = torch.device("cuda")


@skipIfNoCuda
class ConformerFloat64GPUTest(ConformerTestImpl, PytorchTestCase):
    dtype = torch.float64
    device = torch.device("cuda")
