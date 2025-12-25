````markdown
# 🎙️ Zero-Shot Neural Voice Cloning WebUI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-EE4C2C?logo=pytorch)
![Gradio](https://img.shields.io/badge/Gradio-4.0-orange?logo=gradio)
![Hugging Face](https://img.shields.io/badge/Deployment-Hugging%20Face%20Spaces-yellow)

---

## 📑 Abstract

This repository provides a lightweight, browser-based inference interface for **XTTS v2 (Coqui TTS)**, a state-of-the-art autoregressive text-to-speech model. The system supports **zero-shot voice cloning**, allowing voice transfer from a short (~6 second) reference audio clip **without any fine-tuning or retraining**.

The project is designed for easy deployment on **Hugging Face Spaces** (CPU/GPU) and **Google Colab** (GPU), offering both a REST-style inference backend and an interactive **Gradio Web UI**.

---

## 🚀 Key Features

- **Zero-Shot Voice Cloning**  
  Clone a speaker’s voice characteristics from a single short WAV sample.

- **Cross-Lingual Synthesis**  
  Generate speech in up to **16 languages**, independent of the reference audio language.

- **Low-Latency Inference**  
  Optimized for consumer hardware and cloud CPU environments.

- **Interactive Web Interface**  
  Built using **Gradio Blocks** for real-time synthesis and playback.

---

## 🛠️ Technical Architecture

The system is built on **XTTS v2**, which combines:

- **VQ-VAE** – Discrete audio tokenization
- **GPT-style Autoregressive Model** – Predicts audio tokens from text and speaker embeddings
- **HiFi-GAN Decoder** – Converts tokens into high-fidelity waveforms

---

## 📦 Installation & Local Setup

### Prerequisites

- Python **3.9+**
- FFmpeg (available in system path)
- NVIDIA GPU *(optional but recommended for faster inference)*

---

### 1. Clone the Repository

```bash
git clone https://github.com/k-mend/AI-Voice-Clone.git
cd AI-Voice-Clone
````

---

### 2. Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

**Important:** This project depends on strict package versions for compatibility with Coqui TTS.

Example `requirements.txt`:

```text
cython
numpy<2.0
torch==2.4.0
torchaudio==2.4.0
transformers==4.42.4
git+https://github.com/coqui-ai/TTS.git
gradio
```

---

### 3. Run the Application

```bash
python app.py
```

The Gradio interface will be available at:

```
http://127.0.0.1:7860
```

---

## ☁️ Deployment

### Hugging Face Spaces (CPU / Free Tier)

This project is fully compatible with **Hugging Face Spaces**.

1. Create a new Space using the **Gradio SDK**
2. Upload:

   * `app.py`
   * `requirements.txt`
3. The build process will automatically:

   * Download the XTTS v2 model (~2GB)
   * Handle the Coqui CPML license

---

### Google Colab (GPU Acceleration)

For faster inference:

1. Upload the project to Google Colab
2. Set runtime to **T4 GPU**
3. Run the setup and launch commands

---

## 📂 Project Structure

```bash
├── app.py                 # Main Gradio-based inference application
├── requirements.txt       # Dependency list (strict versioning)
├── README.md              # Project documentation
└── output/                # Generated audio files
```

---

## ⚠️ Ethical Usage & License

This project uses the **Coqui Public Model License (CPML)**.

### ✔ Permitted Use

* Personal experimentation
* Academic research
* Open-source development

### ✖ Prohibited Use

* Impersonation without consent
* Deceptive or fraudulent audio generation
* Commercial use without proper licensing

**Disclaimer:**
The maintainers are not responsible for misuse of generated audio. Users are expected to comply with applicable laws and ethical standards.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to submit pull requests for:

* Performance optimizations
* UI improvements
* Additional language support
* Documentation enhancements

---

```
Made with Love for the Opensource Community ❤️
```
