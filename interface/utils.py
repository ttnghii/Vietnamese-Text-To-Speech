from transformers import AutoProcessor, AutoModel
from scipy.io.wavfile import write
import torch

import uuid
import os
import tempfile


# Model
MODEL_NAME = 'suno/bark'
processor = AutoProcessor.from_pretrained(
    pretrained_model_name_or_path=MODEL_NAME
)

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
model = AutoModel.from_pretrained(
    pretrained_model_name_or_path=MODEL_NAME
)
model.to(DEVICE)


def generate_audio(txt: str, preset: str) -> None:
    inputs = processor(txt, voice_preset=preset, return_tensors='pt')
    inputs.to(DEVICE)

    audio_array = model.generate(**inputs, do_sample=True)
    audio_array = audio_array.cpu().numpy().squeeze()

    sample_rate = model.generation_config.sample_rate

    file_id = uuid.uuid1()
    file_path = os.path.join(
        tempfile.gettempdir(),
        f'{file_id}.wav'
    )

    write(file_path, rate=sample_rate, data=audio_array)

    return file_path