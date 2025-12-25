```markdown
# 🎙️ Zero-Shot Neural Voice Cloning WebUI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.4-EE4C2C?logo=pytorch)
![Gradio](https://img.shields.io/badge/Gradio-4.0-orange?logo=gradio)
![Hugging Face](https://img.shields.io/badge/Deployment-Hugging%20Face%20Spaces-yellow)

## 📑 Abstract

This repository implements a lightweight, browser-based inference interface for **XTTS v2 (Coqui TTS)**, a state-of-the-art autoregressive model for text-to-speech synthesis. The system enables **zero-shot voice cloning** (voice transfer) using only a short 6-second reference audio clip, without requiring fine-tuning or model retraining.

The project is containerized for easy deployment on **Hugging Face Spaces** (CPU/GPU) or **Google Colab** (T4 GPU), providing a RESTful API and an interactive GUI via Gradio.

## 🚀 Key Features

* **Zero-Shot Inference:** Clone a target speaker's prosody and timbre from a single ~6s WAV sample.
* **Cross-Lingual Transfer:** Synthesize speech in 16 languages (English, Spanish, French, German, etc.) regardless of the reference audio's original language.
* **Low-Latency Architecture:** Optimized for inference on consumer-grade hardware or cloud-based CPU environments.
* **Interactive Web UI:** Built with Gradio Blocks for real-time audio generation and playback.

## 🛠️ Technical Architecture

The core engine is built upon the **XTTS v2** architecture, which utilizes:
* **VQ-VAE:** Vector Quantized Variational Autoencoder for discrete audio representation.
* **GPT-like Autoregression:** For predicting audio tokens based on input text and speaker latents.
* **HifiGAN Decoder:** For high-fidelity waveform reconstruction.

## 📦 Installation & Local Setup

### Prerequisites
* Python 3.9 or higher
* FFmpeg (installed on system path)
* NVIDIA GPU (Optional, but recommended for <3s inference)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/voice-clone-webui.git](https://github.com/your-username/voice-clone-webui.git)
cd voice-clone-webui

```

### 2. Install Dependencies

This project requires specific versions of PyTorch and Transformers to ensure compatibility with Coqui TTS.

```bash
pip install -r requirements.txt

```

*Note: Ensure your `requirements.txt` contains the following strict versioning:*

```text
cython
numpy<2.0
torch==2.4.0
torchaudio==2.4.0
transformers==4.42.4
git+[https://github.com/coqui-ai/TTS.git](https://github.com/coqui-ai/TTS.git)
gradio

```

### 3. Run Inference

```bash
python app.py

```

The application will launch locally at `http://127.0.0.1:7860`.

## ☁️ Deployment

### Hugging Face Spaces (CPU/Free Tier)

This project is optimized for Hugging Face Spaces.

1. Create a new Space with the **Gradio** SDK.
2. Upload `app.py` and `requirements.txt`.
3. The build pipeline will automatically handle the Coqui CPML license agreement and model download (~2GB).

### Google Colab (GPU Acceleration)

For faster inference using NVIDIA T4 GPUs:

1. Upload the notebook or script to Google Colab.
2. Change runtime type to **T4 GPU**.
3. Run the installation cells to utilize CUDA acceleration.

## 📂 Project Structure

```bash
├── app.py                 # Main inference entry point (Gradio UI)
├── requirements.txt       # Python dependency manifest (Strict versioning)
├── README.md              # Project documentation
└── output/                # (Generated) Directory for synthesized artifacts

```

## ⚠️ Ethical Usage & License

This project utilizes the **Coqui Public Model License (CPML)**.

* **Authorized Use:** Non-commercial research, personal experimentation, and open-source development.
* **Restrictions:** You may not use this software to generate deepfakes for deception, fraud, or impersonation without consent.

**Disclaimer:** The maintainers of this repository are not responsible for misuse of the generated audio. Please use this technology responsibly.

## 🤝 Contributing

Contributions are welcome! Please submit a Pull Request for optimizations, UI enhancements, or additional language support.

```

```
