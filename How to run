# How to Run

This project includes a simple CLI script (`xtts_cli.py`) to generate speech using **Coqui XTTS v2** with a reference speaker.
Note: you'll need a sample.wav file 

---

## 1. Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## 2. Basic Example (Inline Text)

```bash
python3 xtts_cli.py \
  --text "Hello from XTTS running on Jetson Orin Nano." \
  --speaker sample.wav \
  --out output.wav \
  --lang en
```

---

## 3. Using a Text File

```bash
python3 xtts_cli.py \
  --text-file input.txt \
  --speaker sample.wav \
  --out output.wav \
  --lang en
```

---

## 4. Arguments

* `--text` : Text string input
* `--text-file` : Path to a text file
* `--speaker` : Reference speaker WAV file (**required**)
* `--out` : Output file (default: `output.wav`)
* `--lang` : Language code (default: `en`)

---

## 5. Example Folder Structure

```bash
project/
├── xtts_cli.py
├── requirements.txt
├── sample.wav
├── input.txt
├── output.wav
└── venv/
```

---

## 6. Notes

* You must provide either `--text` or `--text-file`
* `--speaker` must be a valid `.wav` file
* The script uses GPU (`cuda`) by default
* First run may take longer (model download)

---

## 7. Verify Output

After running, you should see:

```bash
Saved to output.wav
```

Play it:

```bash
ffplay output.wav
```

or

```bash
aplay output.wav
```
