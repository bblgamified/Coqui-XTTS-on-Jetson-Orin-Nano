# Coqui XTTS on Jetson Orin Nano

This repo documents a working setup for running **Coqui XTTS v2** on an **NVIDIA Jetson Orin Nano** using **JetPack 6.2.x** with **GPU-enabled PyTorch**.

This setup resolves common Jetson issues:
- CPU-only PyTorch installs
- Missing or incompatible `torchaudio`
- `transformers` version conflicts
- XTTS model loading failures
- Speaker WAV file issues
- Power throttling under load

---

## Hardware

- NVIDIA Jetson Orin Nano
- JetPack 6.2.x (L4T R36.x)
- Python 3.10
- Reference voice WAV

---

## Final Working Stack

```text
torch==2.8.0
torchaudio==2.8.0
torchvision==0.23.0
transformers==4.57.6
coqui-tts
