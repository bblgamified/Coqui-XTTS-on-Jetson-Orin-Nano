import argparse
import os
from TTS.api import TTS

parser = argparse.ArgumentParser()
parser.add_argument("--text", help="Text input")
parser.add_argument("--text-file", help="Path to text file")
parser.add_argument("--speaker", required=True)
parser.add_argument("--out", default="output.wav")
parser.add_argument("--lang", default="en")

args = parser.parse_args()

# Validate input
if not args.text and not args.text_file:
    raise ValueError("Provide --text or --text-file")

if args.text_file:
    if not os.path.isfile(args.text_file):
        raise FileNotFoundError(f"Text file not found: {args.text_file}")
    with open(args.text_file, "r") as f:
        text = f.read()
else:
    text = args.text

if not os.path.isfile(args.speaker):
    raise FileNotFoundError(f"Speaker WAV not found: {args.speaker}")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.to("cuda")

tts.tts_to_file(
    text=text,
    speaker_wav=args.speaker,
    language=args.lang,
    file_path=args.out
)

print(f"Saved to {args.out}")
