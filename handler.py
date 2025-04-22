from runpod.serverless.modules.rp_logging import RunPodLogger
import base64
from gtts import gTTS
import tempfile
import os

def handler(event):
    try:
        prompt = event['input']['prompt']

        # 텍스트 → mp3 변환
        tts = gTTS(prompt, lang='ko')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        # mp3를 base64로 인코딩해서 반환
        with open(temp_file.name, "rb") as f:
            audio_data = f.read()
            encoded_audio = base64.b64encode(audio_data).decode("utf-8")

        os.unlink(temp_file.name)
        return {"audio_base64": encoded_audio}

    except Exception as e:
        RunPodLogger.error(str(e))
        return {"error": str(e)}
