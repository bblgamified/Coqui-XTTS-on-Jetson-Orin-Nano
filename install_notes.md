# Install Notes: Coqui XTTS on Jetson Orin Nano

This document walks through the full setup process used to get **Coqui XTTS v2** running on a **Jetson Orin Nano (JetPack 6.2.x)** with GPU acceleration.

## 1. Verify Jetson / JetPack Version

Check the system version:

```bash
cat /etc/nv_tegra_release
```

Example output:

```text
# R36 (release), REVISION: 4.7
```

This corresponds to the JetPack 6.2.x family.

## 2. Create Python Virtual Environment

Install required system packages:

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv virtualenv libopenblas-dev ffmpeg
```

Create and activate a virtual environment:

```bash
python3 -m virtualenv -p python3 ~/venvs/xtts
source ~/venvs/xtts/bin/activate
python -m pip install --upgrade pip
```

## 3. Install Jetson-Compatible PyTorch

**Important:** Do **not** use `pip install torch` directly on Jetson.

Install required system dependencies:

```bash
sudo apt install -y libcusparselt-dev cuda-cupti-12-6
```

Install PyTorch and torchvision:

```bash
python -m pip install torch==2.8.0 torchvision==0.23.0 \
  --index-url https://pypi.jetson-ai-lab.io/jp6/cu126
```

Install matching torchaudio:

```bash
python -m pip install torchaudio==2.8.0 \
  --index-url https://pypi.jetson-ai-lab.io/jp6/cu126
```

## 4. Verify GPU Support

Run:

```bash
python -c "import torch, torchaudio; \
print(torch.__version__); \
print(torchaudio.__version__); \
print(torch.cuda.is_available()); \
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'no cuda')"
```

Expected output:

```text
2.8.0
2.8.0
True
Orin
```

If `False`, stop and fix PyTorch before continuing.

## 5. Install Coqui TTS

```bash
pip install packaging
pip install coqui-tts
```

## 6. Fix Transformers Compatibility Issue

If you encounter:

```text
ImportError: cannot import name 'isin_mps_friendly'
```

Fix it with:

```bash
pip uninstall -y transformers
pip install --no-cache-dir "transformers==4.57.6"
```

## 7. Test Coqui Import

```bash
python -c "from TTS.api import TTS; print('coqui ok')"
```

## 8. Load XTTS Model

Run Python interactively:

```bash
python
```

Then run:

```python
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
tts.to("cuda")

print("XTTS loaded")
```

On first run, accept the license prompt with `y`.

## 9. Generate Speech

```python
tts.tts_to_file(
    text="Hello from my Jetson Orin Nano running XTTS.",
    speaker_wav="/full/path/to/gmm_ref.wav",
    language="en",
    file_path="output.wav"
)
```

## 10. Reference WAV Requirements

Check the file:

```bash
ls -l gmm_ref.wav
file gmm_ref.wav
```

Recommended reference audio:
- 8 to 12 seconds
- clean speech
- single speaker
- low background noise

Convert if needed:

```bash
ffmpeg -i input.wav -ar 24000 -ac 1 -c:a pcm_s16le clean.wav
```

## 11. CLI Workflow

Example usage with inline text:

```bash
python xtts_cli.py \
  --text "Hello world" \
  --speaker /full/path/to/gmm_ref.wav \
  --out test.wav
```

Example usage with a text file:

```bash
python xtts_cli.py \
  --text-file script.txt \
  --speaker /full/path/to/gmm_ref.wav \
  --out test.wav
```

## 12. Monitor System Performance

Use:

```bash
tegrastats
```

Monitor:
- GPU usage (`GR3D_FREQ`)
- RAM
- power draw

## 13. Power / Throttling Issue

Under load, you may see:

```text
System throttled due to over-current
```

Things to try:
- use a 5V / 4–5A power supply
- add cooling such as a fan or heatsink
- reduce USB device load

## 14. Key Issues Encountered

### Missing torch

```text
ModuleNotFoundError: No module named 'torch'
```

Solution: install Jetson-compatible PyTorch.

### 404 PyTorch wheel

Older NVIDIA wheel URLs may fail.

Solution: use the Jetson AI Lab index.

### Missing torchaudio

```text
ModuleNotFoundError: No module named 'torchaudio'
```

Solution: install matching `torchaudio==2.8.0`.

### Transformers import error

```text
ImportError: cannot import name 'isin_mps_friendly'
```

Solution: pin `transformers==4.57.6`.

### XTTS license prompt failure

```text
EOFError
```

Cause: running non-interactively before accepting the XTTS terms.

Solution: run interactively first.

### WAV file error

```text
Failed to open input
```

Solution: fix the file path or WAV format.

## 15. Final Result

Working XTTS setup with:
- GPU acceleration
- stable audio generation
- CLI-based workflow
- text file input support

## 16. Notes

- XTTS reloads the model each run, so the first execution is slower
- shorter reference audio usually improves speed
- GPU usage can be confirmed with `tegrastats`
