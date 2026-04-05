import os
from huggingface_hub import HfApi, create_repo

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = "Rajse/Tourism-Project-Space"

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is not set")

api = HfApi(token=HF_TOKEN)

# Create the Space if it doesn't already exist
create_repo(
    repo_id=REPO_ID,
    repo_type="space",
    space_sdk="gradio",   # change to "streamlit" or "static" if needed
    token=HF_TOKEN,
    exist_ok=True,
)

# Upload your Space files
api.upload_folder(
    folder_path="tourism_project/deployment",
    repo_id=REPO_ID,
    repo_type="space",
    path_in_repo="",
)