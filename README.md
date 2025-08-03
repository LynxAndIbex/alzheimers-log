# alzheimers-log
Alzheimer's Memory Logger
# 🧠 Alzheimer's Memory Logger

An open-source tool designed to preserve and summarize the spoken memories of Alzheimer’s patients — combining voice transcription (Whisper) and summarization (GPT) to support memory care, legacy preservation, and caregiver communication.

## 🚀 Overview

Alzheimer’s often takes away the stories before it takes away the person. This project provides a simple tool for families and caregivers to record a loved one's memories, transcribe them using Whisper, and generate summaries using GPT models — creating a digital memory vault that can be treasured forever.

- 🎙️ Voice recording & upload
- 🔤 Speech-to-text using OpenAI Whisper
- 🧠 Natural language summaries using GPT
- 📁 Local and cloud (optional) memory storage
- 🧓 Designed for non-tech-savvy users and caregivers

## 🎯 Why It Matters

Alzheimer’s impacts over 55 million people globally. Many families struggle to capture meaningful conversations before memories fade. This project aims to:

- Increase patient dignity by preserving their stories
- Reduce caregiver burden by simplifying documentation
- Raise awareness for open-source healthcare solutions

## 🛠️ Tech Stack

- **Frontend**: HTML/CSS/JavaScript (or React, if applicable)
- **Backend**: Python / Flask (or Node.js)
- **Transcription**: [Whisper](https://github.com/openai/whisper)
- **Summarization**: OpenAI GPT (API or open-source alternatives)
- **Storage**: Local or cloud (Firebase / Supabase / S3 optional)

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/alzheimers-memory-logger.git
cd alzheimers-memory-logger
# Setup your environment
pip install -r requirements.txt
# Or follow setup instructions in /docs if using web framework
