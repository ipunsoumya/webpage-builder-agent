import os
import sys
from google.adk.agents import LlmAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.load_file import load_instructions_file

designer_agent = LlmAgent(
    name='designer_agent',
    model='gemini-3.5-flash',
    instruction=load_instructions_file('agents/designer/instructions.txt'),
    description=load_instructions_file('agents/designer/description.txt'),
    output_key='designer_output',
)

