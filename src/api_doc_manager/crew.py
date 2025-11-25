from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ApiDocManagerCrew():
  """ApiDocManager crew"""

  @agent
  def api_doc_manager(self) -> Agent:
    return Agent(
      config=self.agents_config['api_doc_manager'],
      verbose=True
    )

  @task
  def api_doc_manager_task(self) -> Task:
    return Task(
      config=self.tasks_config['api_doc_manager_task'],
      output_file='api_doc.md'
    )

  @crew
  def crew(self) -> Crew:
    """Creates the ApiDocManager crew"""
    return Crew(
      agents=self.agents, # Automatically created by the @agent decorator
      tasks=self.tasks, # Automatically created by the @task decorator
      process=Process.sequential,
      verbose=True,
    )
