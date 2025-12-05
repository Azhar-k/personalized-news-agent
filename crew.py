import os
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv() 
if not os.getenv("GEMINI_API_KEY"):
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit()

# --- 1. Configure the Gemini LLM ---
# The LLM configuration stays in code as it often involves API keys and specific settings
# For CrewAI with LiteLLM, use the format: "gemini/<model-name>"
gemini_llm = "gemini/gemini-2.0-flash-lite"

# --- 2. Define the Crew Base Class ---
# This class handles the loading of the YAML files and assembly of the Crew.
@CrewBase
class HelloCrew:
    """Hello World Crew"""
    
    # Specify the paths to your configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # The @agent decorator looks up the 'greeter' key in agents.yaml
    # and instantiates the Agent object, injecting the defined LLM.
    @agent
    def greeter(self) -> Agent:
        return Agent(
            **self.agents_config['greeter'],
            llm=gemini_llm
        )

    # The @task decorator looks up the 'greeting_task' key in tasks.yaml
    # and instantiates the Task object, assigning it to the agent defined in its config.
    @task
    def greeting_task(self) -> Task:
        return Task(
            **self.tasks_config['greeting_task']
        )

    # The @crew decorator assembles the final Crew object.
    @crew
    def hello_world_crew(self) -> Crew:
        return Crew(
            agents=[self.greeter()],
            tasks=[self.greeting_task()],
            process=Process.sequential,
            verbose=True,
        )

# --- 4. Main execution (often in a separate main.py file) ---
if __name__ == "__main__":
    print("--- Running CrewAI Hello World with Gemini (YAML Config) ---")
    print("-----------------------------------------------------------")

    # Kickoff the crew execution using the CrewBase method
    result = HelloCrew().hello_world_crew().kickoff()

    print("\n\n################################################")
    print("## Final Crew Output")
    print("################################################")
    print(result)