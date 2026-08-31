import os
import sys
from google.adk.agents import LlmAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.load_file import load_instructions_file

_BASE_DIR = os.path.dirname(__file__)

requirement_writer_agent = LlmAgent(
    name='requirement_writer_agent',
    model='gemini-3.5-flash',
    instruction=load_instructions_file(os.path.join(_BASE_DIR, 'instructions.txt')),
    description=load_instructions_file(os.path.join(_BASE_DIR, 'description.txt')),
    output_key='requirement_writer_output',
)