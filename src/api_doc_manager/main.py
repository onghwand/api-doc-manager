#!/usr/bin/env python
import sys
from dotenv import load_dotenv
load_dotenv()
from api_doc_manager.crew import ApiDocManagerCrew

def run():
  """
  Run the crew.
  """
  # This inputs dictionary simulates the data that would be passed 
  # when triggering the agent via an API or GitHub Action.
  # For now, we can default to empty or expect arguments.
  # In a real scenario, you might parse sys.argv or read from a file.
  
  inputs = {
    'source_code_content': 'public class DefaultController {}', # Example default
    'api_spec_path': 'api_spec.yaml'
  }
  
  # Allow overriding via command line args for testing
  if len(sys.argv) > 1:
      file_path = sys.argv[1]
      try:
          with open(file_path, 'r') as f:
              inputs['source_code_content'] = f.read()
      except FileNotFoundError:
          print(f"File not found: {file_path}")
          return

  print(f"Starting crew with inputs: {inputs}")
  try:
      result = ApiDocManagerCrew().crew().kickoff(inputs=inputs)
      print("Crew execution completed.")
      print(f"Result: {result}")
  except Exception as e:
      print(f"Error executing crew: {e}")
      import traceback
      traceback.print_exc()

if __name__ == "__main__":
    run()
