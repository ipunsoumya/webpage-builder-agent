import os
import sys
from google.adk.agents import LlmAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.load_file import load_instructions_file
from tools.file_writer import write_to_file

_BASE_DIR = os.path.dirname(__file__)

code_writer_agent = LlmAgent(
    name='code_writer_agent',
    model='gemini-3.5-flash',
    instruction=load_instructions_file(os.path.join(_BASE_DIR, 'instructions.txt')),
    description=load_instructions_file(os.path.join(_BASE_DIR, 'description.txt')),
    tools=[write_to_file],
)