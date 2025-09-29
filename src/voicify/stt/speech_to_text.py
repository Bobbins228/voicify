#!/usr/bin/env python3
import whisper
from openai import OpenAI
import os
import httpx


class SpeechToText:
    def __init__(self):
        self.whisper_base_url = "https://localhost/v1"
        self.api_key = "API_KEY"
        self.model_name = "whisper-large-v3"

    def speech_to_text(self, wav_path: str):
        unverified_client = httpx.Client(verify=False)

        client = OpenAI(
            base_url=self.whisper_base_url,
            api_key=self.api_key,
            http_client=unverified_client,
        )

        print(f"🚀 Sending '{os.path.basename(wav_path)}' to the Whisper endpoint...")

        try:
            with open(wav_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model=self.model_name, 
                    file=audio_file,
                )

                return transcription.text

        except FileNotFoundError:
            print(f"❌ Error: The file was not found at '{wav_path}'")
        except Exception as e:
            print(f"An API error occurred: {e}")
