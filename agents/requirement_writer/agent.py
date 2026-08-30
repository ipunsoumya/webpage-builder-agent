import os
import sys
from google.adk.agents import LlmAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.load_file import load_instructions_file

requirement_writer_agent = LlmAgent(
    name='requirement_writer_agent',
    model='gemini-3.5-flash',
    instruction=load_instructions_file('agents/requirement_writer/instructions.txt'),
    description=load_instructions_file('agents/requirement_writer/description.txt'),
    output_key='requirement_writer_output',
)