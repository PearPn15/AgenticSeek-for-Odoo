# AgenticSeek-for-Odoo

## Introduction

Odoo is an open-source business management platform that offers a wide range of applications for ERP, CRM, accounting, HR, inventory, and more.

AgenticSeek is an AI assistant designed to run locally, ensuring that enterprise data remains secure and private. It provides intelligent search and Q&A capabilities without exposing sensitive business information to external services.

## Why AgenticSeek?

🔒 Fully Local & Private – Runs entirely on your machine. No cloud, no external data sharing. Your files, conversations, and searches stay private.

🌐 Smart Web Browsing – Can browse the internet autonomously: search, read, extract information, and even fill out web forms.

💻 Autonomous Coding Assistant – Writes, debugs, and runs programs in Python, C, Go, Java, and more — without supervision.

🧠 Smart Agent Selection – Automatically selects the best AI agent for your task, like having a team of experts at your service.

📋 Plans & Executes Complex Tasks – From trip planning to project execution, it can break down tasks into steps and complete them with multiple agents.

🎙️ Voice-Enabled (in progress) – Natural, fast, and futuristic voice interaction, making it feel like your personal AI from a sci-fi movie.

In this project, we integrate AgenticSeek into Odoo at a basic level:

- Users can ask questions directly inside Odoo.

- AgenticSeek provides relevant answers or performs searches within the system context.

- This enhances user productivity by reducing the time needed to find information.

Currently, the integration is limited to Q&A and search assistance, but it lays the foundation for future extensions into automation, decision support, and smart workflows.

<img width="1850" height="1001" alt="image" src="https://github.com/user-attachments/assets/c24d98ce-7b82-4e05-9737-6381d6d5dc7c" />

## How to use my code

### 1. Clone the repository and setup
```
git clone https://github.com/PearPn15/AgenticSeek-for-Odoo.git
cd agenticSeek
mv .env.example .env
```
### 2. Change the .env file content

```
SEARXNG_BASE_URL="http://127.0.0.1:8080"
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/Users/mlg/Documents/workspace_for_ai"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
CUSTOM_ADDITIONAL_LLM_PORT="11435"
OPENAI_API_KEY='optional'
DEEPSEEK_API_KEY='optional'
OPENROUTER_API_KEY='optional'
TOGETHER_API_KEY='optional'
GOOGLE_API_KEY='optional'
ANTHROPIC_API_KEY='optional'
```
Update the .env file with your own values as needed:

- SEARXNG_BASE_URL: Leave unchanged
- REDIS_BASE_URL: Leave unchanged
- WORK_DIR: Path to your working directory on your local machine. AgenticSeek will be able to read and interact with these files.
- OLLAMA_PORT: Port number for the Ollama service.
- LM_STUDIO_PORT: Port number for the LM Studio service.
- CUSTOM_ADDITIONAL_LLM_PORT: Port for any additional custom LLM service.

API Key are totally optional for user who choose to run LLM locally. Which is the primary purpose of this project. Leave empty if you have sufficient hardware

### 3 Star Docker
Make sure Docker is installed and running on your system.
### 4 Installation details for AgenticSeek
https://github.com/Fosowl/agenticSeek
## Setup to run with an API
This setup uses external, cloud-based LLM providers. You'll need an API key from your chosen service.
### 1. Choose an API Provider and Get an API Key
### 2. Set Your API Key as an Environment Variable
- #### Linux/macOS: Open your terminal and use the export command. It's best to add this to your shell's profile file (e.g., ~/.bashrc, ~/.zshrc) for persistence.
- ```export PROVIDER_API_KEY="your_api_key_here" # Replace PROVIDER_API_KEY with the specific variable name, e.g., OPENAI_API_KEY, GOOGLE_API_KEY ```
### 3. Update `config.ini`
```[MAIN]
is_local = False
provider_name = openai # Or google, deepseek, togetherAI, huggingface
provider_model = gpt-3.5-turbo # Or gemini-1.5-flash, deepseek-chat, mistralai/Mixtral-8x7B-Instruct-v0.1 etc.
provider_server_address = # Typically ignored or can be left blank when is_local = False for most APIs
# ... other settings ...
```
## Start services and Run
```
./start_services.sh full # MacOS
start start_services.cmd full # Window
#next
run odoo.bin
```
## Install Agent

<img width="888" height="639" alt="image" src="https://github.com/user-attachments/assets/e2c6eea2-a29b-47cf-be32-4d64d5c6b961" />

<img width="334" height="114" alt="image" src="https://github.com/user-attachments/assets/86d62e4b-1bd5-4e91-af38-e0453d03cd84" />

## Requirements
```
python == 3.11.8
docker == 28.3.2
odoo == v16
kokoro==0.9.4
certifi==2025.4.26
fastapi>=0.115.12
flask>=3.1.0
celery>=5.5.1
aiofiles>=24.1.0
uvicorn>=0.34.0
pydantic>=2.10.6
pydantic_core>=2.27.2
setuptools>=75.6.0
sacremoses>=0.0.53
requests>=2.31.0
numpy>=1.24.4
colorama>=0.4.6
python-dotenv>=1.0.0
playsound3>=1.0.0
soundfile>=0.13.1
transformers>=4.46.3
torch>=2.4.1
ollama>=0.4.7
scipy>=1.9.3
soundfile>=0.13.1
protobuf>=3.20.3
termcolor>=2.4.0
pypdf>=5.4.0
ipython>=8.13.0
pyaudio>=0.2.14
librosa>=0.10.2.post1
selenium>=4.27.1
markdownify>=1.1.0
text2emotion>=0.0.5
adaptive-classifier>=0.0.10
langid>=1.1.6
chromedriver-autoinstaller>=0.6.4
httpx>=0.27,<0.29
anyio>=3.5.0,<5
distro>=1.7.0,<2
jiter>=0.4.0,<1
fake_useragent>=2.1.0
selenium_stealth>=1.0.6
undetected-chromedriver>=3.5.5
sentencepiece>=0.2.0
together>=1.5.0
tqdm>4
openai
sniffio
ordered_set
pypinyin
```
