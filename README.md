{
  "project_name": "System Health Reporter",
  "description": "A System Health Reporter tool developed as part of the Atomixtools Software Developer Intern assignment. The tool collects CPU, memory, and disk usage metrics and outputs them in JSON format. The project is Dockerized for easy execution.",
  "author": {
    "name": "Manvithareddyk",
    "github": "https://github.com/manvithareddyk"
  },
  "tech_stack": [
    "Python 3",
    "Docker",
    "Git",
    "GitHub"
  ],
  "features": [
    "CPU usage monitoring",
    "Memory usage monitoring",
    "Disk usage monitoring",
    "JSON formatted output",
    "Verbose execution mode",
    "Dockerized CLI tool"
  ],
  "project_structure": {
    "system-health-reporter": {
      "app": {
        "main.py": "Main Python script that collects and prints system health metrics"
      },
      "Dockerfile": "Docker configuration file to build the container image",
      "requirements.txt": "Python dependencies required for the project",
      "README.md": "Project documentation and usage instructions"
    }
  },
  "prerequisites": {
    "python": "Python 3.8 or above",
    "docker": "Docker installed and running",
    "git": "Git installed"
  },
  "local_execution": {
    "clone_repository": [
      "git clone git@github.com:manvithareddyk/system-health-reporter.git",
      "cd system-health-reporter"
    ],
    "virtual_environment_optional": [
      "python -m venv venv",
      "source venv/bin/activate"
    ],
    "install_dependencies": [
      "pip install -r requirements.txt"
    ],
    "run_application": [
      "python app/main.py"
    ],
    "run_verbose_mode": [
      "python app/main.py --verbose"
    ]
  },
  "docker_execution": {
    "build_image": [
      "docker build -t system-health-reporter ."
    ],
    "run_container": [
      "docker run system-health-reporter"
    ]
  },
  "output_format_example": {
    "cpu_usage": "15%",
    "memory_usage": "45%",
    "disk_usage": "60%"
  },
  "git_workflow": {
    "branching_strategy": "Feature branch workflow",
    "pull_request": "All changes are submitted via Pull Request for review",
    "merge_policy": "Pull Request is left unmerged for reviewer evaluation"
  },
  "assignment_notes": [
    "This project was created for the Atomixtools Software Developer Intern assignment",
    "Demonstrates system monitoring, Docker usage, and Git workflow",
    "Pull Request link is shared as the final submission"
  ],
  "license": "Educational and assignment use only"
}
