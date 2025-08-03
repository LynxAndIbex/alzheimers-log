import gradio as gr
import whisper
import json
import os
from datetime import datetime

model = whisper.load_model("base")

def transcribe(audio_filepath):
    result = model.transcribe(audio_filepath)
    return result["text"]

def poeticize(text):
    return (
        f"In whispers soft and shadows deep,\n"
        f"Memory wakes from silent sleep.\n"
        f"Echoes dance in time’s embrace,\n"
        f"Words transformed with gentle grace.\n\n"
        f"Original thought:\n{text}"
    )

def save_memory(memory_text, filename):
    memories_file = "memories.json"
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "filename": filename,
        "memory_text": memory_text
    }
    if os.path.exists(memories_file):
        with open(memories_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(new_entry)

    with open(memories_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def transcribe_and_poeticize(audio_filepath):
    transcript = transcribe(audio_filepath)
    poetic_memory = poeticize(transcript)
    save_memory(poetic_memory, os.path.basename(audio_filepath))
    return transcript, poetic_memory

def load_memories():
    memories_file = "memories.json"
    if os.path.exists(memories_file):
        with open(memories_file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                formatted = ""
                for i, mem in enumerate(data, 1):
                    formatted += f"Memory {i} (from {mem['filename']} at {mem['timestamp']}):\n"
                    formatted += mem['memory_text'] + "\n\n"
                return formatted
            except json.JSONDecodeError:
                return "Error loading memories: JSON corrupted."
    else:
        return "No memories saved yet."

def delete_memory(index_str):
    memories_file = "memories.json"
    if not os.path.exists(memories_file):
        return "No memories to delete.", ""

    try:
        index = int(index_str) - 1
    except ValueError:
        return "Please enter a valid number.", ""

    with open(memories_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return "Error reading memories file.", ""

    if index < 0 or index >= len(data):
        return "Index out of range.", ""

    deleted = data.pop(index)

    with open(memories_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    updated_memories = ""
    for i, mem in enumerate(data, 1):
        updated_memories += f"Memory {i} (from {mem['filename']} at {mem['timestamp']}):\n"
        updated_memories += mem['memory_text'] + "\n\n"

    return f"Deleted memory {index + 1}: {deleted['filename']}", updated_memories

def get_memories_file():
    memories_file = "memories.json"
    if os.path.exists(memories_file):
        return memories_file
    else:
        return None

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🧠 Alzheimer's Memory Logger
        Upload or record an audio memory to transcribe and create a poetic memory.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            audio_input = gr.Audio(
                sources=["microphone", "upload"],  # Allow recording or uploading
                type="filepath",
                label="Record or Upload Audio"
            )
            submit_btn = gr.Button("Transcribe & Poeticize", variant="primary")
            
            gr.Markdown("### Delete a Memory")
            delete_input = gr.Textbox(label="Memory Number to Delete", placeholder="Enter memory number here")
            delete_btn = gr.Button("Delete Memory", variant="danger")
            delete_msg = gr.Textbox(label="Delete Status", interactive=False)
            
            download_btn = gr.Button("Download All Memories")
            download_file = gr.File(label="Download Memories File")
        
        with gr.Column(scale=2):
            transcript_output = gr.Textbox(label="Transcript", lines=6)
            poetic_output = gr.Textbox(label="Poetic Memory", lines=10)
            view_btn = gr.Button("View Saved Memories")
            memories_output = gr.Textbox(label="Saved Memories", lines=15)

    submit_btn.click(
        fn=transcribe_and_poeticize,
        inputs=audio_input,
        outputs=[transcript_output, poetic_output]
    )

    view_btn.click(
        fn=load_memories,
        inputs=None,
        outputs=memories_output
    )

    delete_btn.click(
        fn=delete_memory,
        inputs=delete_input,
        outputs=[delete_msg, memories_output]
    )

    download_btn.click(
        fn=get_memories_file,
        inputs=None,
        outputs=download_file
    )

demo.launch()
