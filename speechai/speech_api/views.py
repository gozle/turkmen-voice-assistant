import logging
import os
from datetime import datetime
from pydub import AudioSegment

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.asr import EnglishAsrInitialising, RussianAsrInitialising
from speechai.settings.base import BASE_DIR

logger = logging.getLogger(__name__)


@csrf_exempt
def english_asr(request):
    data = request.body
    filename = (
        os.path.join(BASE_DIR, "audio/")
        + "english_asr"
        + datetime.now().strftime("%Y%m%d_%H%M")
        + ".wav"
    )

    with open(filename, "wb") as f:
        f.write(data)

    try:
        logger.info(f"Filename is {filename}")
        audio_f = AudioSegment.from_wav(filename)
        logger.info(
            f"Input file parameters {audio_f.frame_rate} and {audio_f.channels}"
        )

        if audio_f.frame_rate != 16000:
            audio_f = audio_f.set_frame_rate(16000)
            logger.info("Changed audio file frame_rate to 16000")

        if audio_f.channels != 1:
            audio_f = audio_f.set_channels(1)
            logger.info("Changed audio file channels to 1")

        audio_f.export(filename, format="wav")
        logger.info(f"{audio_f.frame_rate} and {audio_f.channels}")

    except Warning:
        logger.info("Audio is in good format")
        pass

    asr_output = EnglishAsrInitialising.asr_model.trancribe([filename])
    msg = {"text": asr_output[0]}
    logger.info(f"{asr_output}" + " NLP ->" + f"{asr_output[0]}")

    return JsonResponse(msg)


@csrf_exempt
def rus_asr(request):
    data = request.body
    filename = (
        os.path.join(BASE_DIR, "audio/")
        + "russian_asr"
        + datetime.now().strftime("%Y%m%d_%H%M")
        + ".wav"
    )

    with open(filename, "wb") as f:
        f.write(data)

    try:
        logger.info(f"Filename is {filename}")
        audio_f = AudioSegment.from_wav(filename)
        logger.info(
            f"Input file parameters {audio_f.frame_rate} and {audio_f.channels}"
        )

        if audio_f.frame_rate != 16000:
            audio_f = audio_f.set_frame_rate(16000)
            logger.info("Changed audio file frame_rate to 16000")

        if audio_f.channels != 1:
            audio_f = audio_f.set_channels(1)
            logger.info("Changed audio file channels to 1")

        audio_f.export(filename, format="wav")
        logger.info(f"{audio_f.frame_rate} and {audio_f.channels}")

    except Warning:
        logger.info("Audio is in good format")
        pass

    asr_output = RussianAsrInitialising.asr_model.trancribe([filename])
    msg = {"text": asr_output[0]}
    logger.info(f"{asr_output}" + " NLP ->" + f"{asr_output[0]}")

    return JsonResponse(msg)
