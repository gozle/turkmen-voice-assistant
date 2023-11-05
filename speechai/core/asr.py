import torch
import nemo.collections.asr as nemo_asr
import gc
import logging
import os
from speechai.speechai.settings.base import MODELS_ROOT

logger = logging.getLogger(__name__)


class EnglishAsrInitialising:
    def __init__(self, torch_device=None):
        if torch_device is None:
            if torch.cuda.is_available():
                torch_device = torch.device("cuda")
            else:
                torch_device = torch.device("cpu")

    try:
        gc.collect()
        torch.cuda.empty_cache()
        name = "eng_asr"
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from(
            restore_path=os.path.join(MODELS_ROOT, "stt_en_conformer_ctc_xlarge.nemo"),
            map_location=device,
        )

    except FileNotFoundError as e:
        logger.critical(e)
        logger.critical("Could not load English CTC model")

    def covert_to_text(self, audio_files):
        return self.asr_model.transcribe(paths2audio_files=audio_files)


class RussianAsrInitialising:
    def __init__(self, torch_device=None):
        if torch_device is None:
            if torch.cuda.is_available():
                torch_device = torch.device("cuda")
            else:
                torch_device = torch.device("cpu")

    try:
        gc.collect()
        torch.cuda.empty_cache()
        name = "rus_asr"
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        asr_model = nemo_asr.models.EncDecCTCModelBPE.restore_from(
            restore_path=os.path.join(MODELS_ROOT, "stt_ru_quartznet15x5.nemo"),
            map_location=device,
        )

    except FileNotFoundError as e:
        logger.critical(e)
        logger.critical("Could not load Rus CTC model")

    def covert_to_text(self, audio_files):
        return self.asr_model.transcribe(paths2audio_files=audio_files)


# """
#         self.file_config = path.join(WORK_DIR, _MODEL_CONFIG)
#         self.file_checkpoints = path.join(WORK_DIR, _MODEL_WEIGHTS)

#         model_config = OmegaConf.load(self.file_config)
#         OmegaConf.set_struct(model_config, True)

#         if isinstance(model_config, DictConfig):
#             self.config = OmegaConf.to_container(model_config, resolve=True)
#             self.config = OmegaConf.create(self.config)
#             OmegaConf.set_struct(self.config, True)

#         # EncDecCTCModel.set_model_restore_state(is_being_restored=True)
#         instance = EncDecCTCModel(cfg=self.config)

#         self.model_instance = instance
#         self.model_instance.to(torch_device)
#         self.model_instance.load_state_dict(torch.load(self.file_checkpoints, torch_device), False)

# """
