import os
import torch
from TTS.api import TTS
import gradio as gr

# 1. SETUP: License & Device
# We must agree to the license programmatically to avoid a prompt stopping the app
os.environ["COQUI_TOS_AGREED"] = "1"

# Check for GPU (Free Spaces are usually CPU, but this code works for both)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Running on: {device}")

# 2. MODEL: Load the XTTS Model
# This will download the model (~2GB) on the first run.
# Hugging Face caches it, so future restarts are faster.
print("⏳ Loading XTTS Model... please wait.")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
print("✅ Model Loaded!")

# 3. CORE FUNCTION
def clone_voice(text, audio_file_path, language):
    if not text or not audio_file_path:
        return None, "Please provide both text and a reference audio."
        
    output_path = "output_cloned.wav"
    
    # Clean up previous file
    if os.path.exists(output_path):
        os.remove(output_path)
    
    try:
        # Run TTS
        tts.tts_to_file(
            text=text,
            speaker_wav=audio_file_path,
            language=language,
            file_path=output_path
        )
        return output_path, "Success! Audio generated."
    except Exception as e:
        return None, f"Error: {str(e)}"

# 4. INTERFACE
with gr.Blocks(title="AI Voice Cloner") as demo:
    gr.Markdown("# 🎙️ Free AI Voice Cloner")
    gr.Markdown("Clone any voice from a 6-second sample. Running on Hugging Face Spaces.")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Text to Speak", value="Hello! This is a voice clone running on the cloud for free.")
            
            # XTTS supports these specific languages
            language_dropdown = gr.Dropdown(
                choices=["en", "es", "fr", "de", "it", "pt", "pl", "tr", "ru", "nl", "cs", "ar", "zh-cn", "ja", "hu", "ko"], 
                value="en", 
                label="Language"
            )
            
            ref_audio = gr.Audio(label="Reference Voice (Upload 6s wav)", type="filepath")
            generate_btn = gr.Button("Generate Voice", variant="primary")
            
        with gr.Column():
            audio_output = gr.Audio(label="Result")
            status_output = gr.Textbox(label="Status", interactive=False)

    generate_btn.click(
        fn=clone_voice,
        inputs=[text_input, ref_audio, language_dropdown],
        outputs=[audio_output, status_output]
    )

# Launch the app
demo.launch()