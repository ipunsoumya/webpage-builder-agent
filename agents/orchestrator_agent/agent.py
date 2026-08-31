import os
import sys
from google.adk.agents import SequentialAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.load_file import load_instructions_file
from agents.designer.agent import designer_agent
from agents.requirement_writer.agent import requirement_writer_agent
from agents.code_writer.agent import code_writer_agent

_BASE_DIR = os.path.dirname(__file__)

root_agent = SequentialAgent(
    name='orchestrator_agent',
    sub_agents=[requirement_writer_agent, designer_agent, code_writer_agent],
    description=load_instructions_file(os.path.join(_BASE_DIR, 'description.txt'))
)